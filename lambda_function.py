import json
from jsonschema import validate, ValidationError


def lambda_handler(event, context):
 

    with open('verified_claims_request-09.json') as file_obj:
        json_schema = json.load(file_obj)


    list1 = ['eKYC-IDA-5.1.a.json',
        'eKYC-IDA-5.1.b.json',
        'eKYC-IDA-5.1.c.json',
        'eKYC-IDA-5.2.a.json',
        'eKYC-IDA-5.2.b.json',
        'eKYC-IDA-5.2.c.json',
        'eKYC-IDA-5.3.1.json',
        'eKYC-IDA-5.3.2.json',
        'eKYC-IDA-6.5.1.json',
        'eKYC-IDA-6.6.1.json',
        'eKYC-IDA-5.1.c_too_long.json', 
        'eKYC-IDA-5.1.c_too_short.json',
        'eKYC-IDA-5.1.c_wrong_essencial_type.json']
    for item in list1:

        print("validating: >>>>>>>>>>>>>>>>>>>>")
        print(item)
        with open(item) as data_file_obj:
            json_data = json.load(data_file_obj)
        try:
            validate(json_data, json_schema)
        except ValidationError as e:
            print(e.message)
            print("xxxxxxxxxxxxxxxx  "+item+" is INVALID")
        else:
            print(">>>>>>>>>>>>>>>>  "+item+" is valid")



