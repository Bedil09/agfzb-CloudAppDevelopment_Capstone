import sys
fromcloudant.clientimportCloudant
fromcloudant.errorimportCloudantException


def main(dict):

    screat = {
        "COUCH_URL": "https://f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY": "hhLIBg18IlcYe-ir_xf6aXAt3prqG4zNRjY_GDLAJwAH",
        "COUCH_USERNAME": "f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix"
    }

    client = Cloudant(
        screat["COUCH_USERNAME"],
        screat["IAM_API_KEY"],
        url=screat["COUCH_URL"],
        connect=True,
    )

    databaseName = "reviews"
    try:

        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )

        reviews = client[databaseName]
    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce, "code": 500}

    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err, "code": 500}

    if "review" in dict.keys():
        my_document = reviews.create_document(dict['review'])
        if my_document.exists():
            return my_document

    elif "dealerId" in dict.keys():
        selector = {"dealership": {"$eq": int(dict['dealerId'])}}
        query = Query(reviews, fields=['id', 'name', 'dealership', 'review', 'purchase',
                                       'purchase_date', 'car_make', 'car_model', 'car_year'], selector=selector)
        results = []
        for result in QueryResult(query):
            results.append(result)
        if results:
            return {
                "body": results
            }
        else:
            return {
                "error":
                    {
                        "code": 404,
                        "message": "dealerId does not exist"
                    }
            }
