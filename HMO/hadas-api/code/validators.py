
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

def validate_records(customer_id,text_vars:list,int_vars:list,date_vars:list):
    #NOTE: we can also add length validation for home+cell numbers
    valid = True
    message = None
    #validate customer_id
    if len(customer_id) != 9:
        valid = False
        message = "customer ID must be a 9-digit long integer"
        return valid,message
    # Check date format
    for date in date_vars:
        if date:
            if not validate_dates(date):
                valid = False
                message = "date field is not in 'DD-MM-YYYY' format"
                return valid, message
    #Check string format
    for var in text_vars:
        if var:
            if not isinstance(var,str):
                valid = False
                message = f"{var} is not a string"
                return valid, message
    #Check integer format
    for var in int_vars:
        if var:
            if not isinstance(int(var),int):
                valid = False
                message = f"{var} is not an integer"
                return valid, message
    return valid, message


def validate_dates(date):
    try:
        valid = bool(datetime.strptime(date, "%d-%m-%Y"))
    except Exception:
        valid = False
    return valid


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
