# Hadas-API: Corona Database

Hadas-API is a client-facing API meant to query and upload personal and Corona-related data. Hadas-API includes the following capabitiles:
- Uploading new records to **customer_data**
- Uploading new records to **corona_data**
- Querying data from a joint table of both **corona_data** and **customer_data**
- Querying by specific fields from database
- Uploading customer images 
- Viewing customer image by customer_id

Used technologies: Flask + SQLite (Python)

## Installation

To start the server, run:
```bash
python run.py
```
The server will run under localhost:8000

## Project Structure
```
.
├── code
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── graphs.py
│   ├── run.py
│   ├── services.py
│   └── validators.py
├── data
│   └── hadas.db
├── requirements.txt
└── uploads
```

## Database

The database, **hadas.db**, has two main tables that are linked by the column **customer_id**

### customer_data
contains the following fields (all mandatory):

``` json
    "customer_id": integer,
    "fullname": string,
    "date_of_birth": date in DD-MM-YYYY format,
    "home_number": integer,
    "cellphone_number": integer,
    "address": string
```
### corona_data
contains the following fields (customer_id, first_vac and first_vac_manu are mandatory):
``` json
    "customer_id": integer,
    "first_vac": date in DD-MM-YYYY format,
    "first_vac_manu": string,
    "second_vac": date in DD-MM-YYYY format,
    "second_vac_manu": string,
    "third_vac": date in DD-MM-YYYY format,
    "third_vac_manu": string,
    "fourth_vac": date in DD-MM-YYYY format,
    "fourth_vac_manu": string
    "date_of_infection": date in DD-MM-YYYY format,
    "date_of_recovery": date in DD-MM-YYYY format
```

## Requests

### Upload New Records to customer_data (POST)
**URL:**`localhost:8000/insertCustomerRecord`

### Upload New Records to corona_data (POST)
**URL:**`localhost:8000/insertCoronaRecord`

### Query Table Data (GET)
**URL:**`localhost:8000/queryCustomerData`

### Query Specific Field (GET)
**URL:**`localhost:8000/queryCustomerData`
```json
"field":required_field,
"value":required_value
```
### Upload Customer Photo
**URL:**`localhost:8000/uploadCustomerPhoto`
```json
"file":image_file_path,
"customer_id":customer_id
```
### Get Customer Photo by customer_id
**URL:**`localhost:8000/getCustomerPhoto/<customer_id>`
