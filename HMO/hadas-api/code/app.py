from flask import Flask
import os
from services import (
    add_person_service,
    add_corona_info_service,
    get_all_records_service,
    query_record_service,
    upload_file_service,
    get_file_service
)

app = Flask(__name__)


@app.route("/insertCustomerRecord", methods=["POST"])
def add_person():
    return add_person_service()


@app.route("/insertCoronaRecord", methods=["POST"])
def add_corona_info():
    return add_corona_info_service()


@app.route("/getAllCustomersRecord")
def get_all_records():
    return get_all_records_service()


@app.route("/queryCustomerData", methods=["GET"])
def query_record():
    return query_record_service()


@app.route("/uploadCustomerPhoto", methods=["POST"])
def upload_file():
    return upload_file_service()

    
@app.route("/getCustomerPhoto/<customer_id>")
def get_file(customer_id):
    return get_file_service(customer_id)
