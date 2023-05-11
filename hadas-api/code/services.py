from flask import jsonify, request, send_from_directory
from database import get_db
from validators import validate_records, allowed_file, MAX_CONTENT_LENGTH
from werkzeug.utils import secure_filename
import os
import json

UPLOADS_DIRECTORY = "../uploads"


def add_person_service():
    data = request.get_json(force=True)

    # TODO: create correct records
    customer_id = data.get("customer_id")
    fullname = data.get("fullname")
    address = data.get("address")
    date_of_birth = data.get("date_of_birth")
    home_number = data.get("home_number")
    cellphone_number = data.get("cellphone_number")
    # Divide variables into formats
    text_vars = [fullname, address]
    int_vars = [customer_id, home_number, cellphone_number]
    date_vars = [date_of_birth]
    # Check if all fields are present
    if not any(data.values()):
        return jsonify(
            {
                "message": """At least one field is missing.\n Please fill out all the following fields:customer_id,
    fullname,
    address,
    date_of_birth,
    home_number,
    cellphone_number"""
            }
        )
    # Validate all records
    valid, message = validate_records(
        customer_id=customer_id,
        text_vars=text_vars,
        date_vars=date_vars,
        int_vars=int_vars,
    )
    if not valid:
        return jsonify({"message": f"{message}"}), 400
    # Activate DB
    else:
        db = get_db()
        cur = db.cursor()
        # Check if ID already exists, if it is - abort
        cur.execute(f"SELECT * FROM customer_data WHERE customer_id={customer_id}")
        existing_person = cur.fetchone()
        if existing_person:
            return jsonify(
                {"message": f"This ID already exists in our customer's table"}
            )
        cur.execute(
            """
        INSERT INTO customer_data
        (customer_id,
        fullname,
        address,
        date_of_birth,
        home_number,
        cellphone_number) VALUES (?, ?, ?, ?, ?, ?) """,
            (
                customer_id,
                fullname,
                address,
                date_of_birth,
                home_number,
                cellphone_number,
            ),
        )
        db.commit()
        cur.close()

        return jsonify({"message": f"Customer {customer_id} added to database."}), 200


def add_corona_info_service():
    mandatory_keys = ["customer_id", "first_vac", "first_vac_manu"]
    # load data to JSON
    data = request.get_json(force=True)

    customer_id = data.get("customer_id")
    first_vac = data.get("first_vac")
    first_vac_manu = data.get("first_vac_manu")
    second_vac = data.get("second_vac")
    second_vac_manu = data.get("second_vac_manu")
    third_vac = data.get("third_vac")
    third_vac_manu = data.get("third_vac_manu")
    fourth_vac = data.get("fourth_vac")
    fourth_vac_manu = data.get("fourth_vac_manu")
    date_of_infection = data.get("date_of_infection")
    date_of_recovery = data.get("date_of_recovery")

    # Check if first_vac + first_vac_manu exist
    if not any(mandatory_keys):
        return jsonify(
            {"message": "Please fill out at least first vaccine date and manufacturer"}
        )
    # if not any([first_vac, first_vac_manu]) or not customer_id:

    # Divide variables into formats
    text_vars = [first_vac_manu, second_vac_manu, third_vac_manu, fourth_vac_manu]
    int_vars = [customer_id]
    date_vars = [first_vac, second_vac, third_vac, fourth_vac, date_of_infection, date_of_recovery]
    # Validate all records
    valid, message = validate_records(
        customer_id=customer_id,
        text_vars=text_vars,
        date_vars=date_vars,
        int_vars=int_vars,
    )
    if not valid:
        return jsonify({"message": f"{message}"}), 400
    # Activate DB
    else:
        db = get_db()
        cur = db.cursor()

        # Check if ID already exists, if not - abort
        cur.execute(f"SELECT * FROM customer_data WHERE customer_id={customer_id}")
        existing_person = cur.fetchone()
        if not existing_person:
            return jsonify(
                {"message": f"This ID does not exist in our customer's table"}
            )
        # Check if there's already an existing record in corona_data
        cur.execute(f"SELECT * FROM corona_data WHERE customer_id={customer_id}")
        existing_person = cur.fetchone()
        if existing_person:
            return jsonify({"message": f"This ID already exists in corona_data"})
        else:
            cur.execute(
                """
            INSERT INTO corona_data
            (customer_id,
            first_vac,
            first_vac_manu,
            second_vac,
            second_vac_manu,
            third_vac,
            third_vac_manu,
            fourth_vac,
            fourth_vac_manu,
            date_of_infection,
            date_of_recovery) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """,
                (
                    customer_id,
                    first_vac,
                    first_vac_manu,
                    second_vac,
                    second_vac_manu,
                    third_vac,
                    third_vac_manu,
                    fourth_vac,
                    fourth_vac_manu,
                    date_of_infection,
                    date_of_recovery

                ),
            )
        db.commit()
        cur.close()
        return jsonify(
            {"message": f"Customer's {customer_id} corona data added to corona_data."}
        )


def get_all_records_service():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM customer_data LEFT JOIN corona_data using(customer_id)")
        
    # Fetch all rows as a list of tuples
    rows = cur.fetchall()
    # Get the column names of the table
    column_names = [description[0] for description in cur.description]
    # Create a list of dictionaries, where each dictionary represents a row in the table
    result = []
    for row in rows:
        row_dict = {}
        for i, column_name in enumerate(column_names):
            row_dict[column_name] = row[i]
        result.append(row_dict)

    return jsonify(result)


def query_record_service():
    field = request.json["field"]
    value = request.json["value"]
    db = get_db()
    cur = db.cursor()
    cur.execute(
        f"SELECT * FROM customer_data LEFT JOIN corona_data using(customer_id) WHERE {field} = '{value}' "
    )
    response = cur.fetchone()
    if response is None:
        return jsonify({"message":"No records correlating with this customer_id"})

    # Get the column names of the table
    column_names = [description[0] for description in cur.description]

    result = {}
    for i, column_name in enumerate(column_names):
        result[column_name] = response[i]
    cur.close()
    return jsonify(result)


def upload_file_service():
    valid,message = validate_records(request.files)
    if not valid:
        return jsonify({"error":message}),400

    file = request.files["file"]
    file.seek(0)
    customer_id = request.form.get("customer_id")

    # Check if ID already exists, if not - abort
    db = get_db()
    cur = db.cursor()
    cur.execute(f"SELECT * FROM customer_data WHERE customer_id={customer_id}")
    existing_person = cur.fetchone()
    if not existing_person:
        return jsonify({"message": f"This ID does not exist in our customer's table"})
    if not customer_id:
        return {"error": "Missing 'customer_id' parameter"}, 400

    filename = secure_filename(f"{customer_id}.png")
    file.save(os.path.join(UPLOADS_DIRECTORY, filename))

    return {"message": "Uploaded successfully"}


def get_file_service(customer_id):
    filename = secure_filename(f"{customer_id}.png")
    return send_from_directory(UPLOADS_DIRECTORY, filename)


