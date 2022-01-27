from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(dict):

    secret = {
        "COUCH_URL": "https://f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix.cloudantnosqldb.appdomain.cloud",
        "COUCH_USERNAME": "f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix",
        "IAM_API_KEY": "hhLIBg18IlcYe-ir_xf6aXAt3prqG4zNRjY_GDLAJwAH",
    }

    client = Cloudant.iam(
        account_name=secret["COUCH_USERNAME"],
        api_key=secret["IAM_API_KEY"],
        connect=True,
    )

    my_database = client["reviews"]

    try:
        selector = {'id': {'$eq': int(dict["id"])}}
        rows = my_database.get_query_result(
            selector, fields=['id', 'name', 'dealership', 'review', 'purchase',
                              'purchase_date', 'car_make', 'car_model', 'car_year'], raw_result=True)

        result = {
            'body': {'data': rows}
        }

        return result

    except:

        return {
            'statusCode': 404,
            'message': 'Something went wrong',
        }
