import re



class RegexHandler:


    def __init__(self) -> None:
        pass

    def validate_email(self, str2check: str) -> bool:
        """Check if the given string is an email"""
        pattern = r"^[a-zA-Z.]+@([a-zA-Z]+\.)+[a-zA-Z]+$"
        return bool(re.search(pattern, str2check))
    
    def validate_phone(self, str2check: str) -> bool:
        """Check if the given string is a phone number"""
        pattern = r"^(61|\(61\))0[0-9]{9}$"
        return bool(re.search(pattern, str2check))

def read_csv(csv_fpath: str):
    """
    Read a CSV file and return a list of dict. Each dict represents a row. The key of the dict
    is the header string, and the value of the dict is the cell value. 
    """
    
    rows = [] 

    with open(csv_fpath, 'r') as f:
        lines = f.read().split("\n")
        
        header_line: str = lines[0]
        header_list = header_line.split(',')

        for line in lines[1:]:
            if not line:
                continue

            row_list = line.split(',')
            row_dict = {}

            for header, value in zip(header_list, row_list):
                row_dict[header] = value 

            rows.append(row_dict)

    return rows 


def read_props(prop_fpath: str) -> dict:
    """
    Read a CSV file and return a dict that maps property id to property address.
    """
    
    id_to_address = {}
    for row in read_csv(prop_fpath):
        id_to_address[row['prop_id']] = row['full_address']
    return id_to_address
    

def read_email(email_fpath: str) -> dict:
    """
    Read a CSV file and return a dict that maps property id to email.
    """

    id_to_email = {}
    for row in read_csv(email_fpath):
        id_to_email[row['prop_id']] = row['email']
    return id_to_email

def read_phone(phone_fpath: str) -> dict:
    """
    Read a CSV file and return a dict that maps property id to phone.
    """

    id_to_phone = {}
    for row in read_csv(phone_fpath):
        id_to_phone[row['prop_id']] = row['phone']
    return id_to_phone

def prop_email_matcher(prop_fpath: str, email_fpath: str) -> str:
    """
    Match the email address, then linking the data back to the original 
    property, and adding the email address to the original CSV data
    """
    id_to_address = read_props(prop_fpath)
    id_to_email = read_email(email_fpath)

    re_handler = RegexHandler()

    rows = []
    rows.append('prop_id,full_address,email')

    for prop_id, address in id_to_address.items():
        if prop_id not in id_to_email:
            continue 

        email = id_to_email[prop_id]
        if not re_handler.validate_email(email):
            email = ""

        row = prop_id + "," + address + "," + email
        rows.append(row)

    return '\n'.join(rows)


def prop_phone_matcher(prop_fpath: str, phone_fpath: str) -> str:
    """
    Match the phone, then linking the data back to the original 
    property, and adding the phone to the original CSV data
    """

    id_to_address = read_props(prop_fpath)
    id_to_phone = read_phone(phone_fpath)

    re_handler = RegexHandler()

    rows = []
    rows.append('prop_id,full_address,phone')

    for prop_id, address in id_to_address.items():
        if prop_id not in id_to_phone:
            continue 
        
        phone = id_to_phone[prop_id]
        if not re_handler.validate_phone(phone):
            phone = ""

        row = prop_id + "," + address + "," + phone
        rows.append(row)

    return '\n'.join(rows)

def merge_prop_email_phone(prop_fpath: str, email_phone_fpath: str) -> str:
    """
    Match the email address and phone, then linking the data back to the original 
    property, and adding the email and phone to the original CSV data
    """

    id_to_address = read_props(prop_fpath)
    id_to_email = read_email(email_phone_fpath)
    id_to_phone = read_phone(email_phone_fpath)

    re_handler = RegexHandler()

    rows = []
    rows.append('prop_id,full_address,email,phone')

    for prop_id, address in id_to_address.items():
        if prop_id not in id_to_email:
            continue 
        if prop_id not in id_to_phone:
            continue 

        email = id_to_email[prop_id]
        if not re_handler.validate_email(email):
            email = ""

        phone = id_to_phone[prop_id]
        if not re_handler.validate_phone(phone):
            phone = ""          
        
        if email == "" and phone == "":
            continue

        row = prop_id + "," + address + "," + email + "," + phone
        rows.append(row)
    
    return '\n'.join(rows)


if __name__ == "__main__":
    print("Task 1 results: ")
    print(prop_email_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 2 results: ")
    print(prop_phone_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 3 results: ")
    print(merge_prop_email_phone("sample_properties.csv", "sample_properties_email_phone.csv"))

