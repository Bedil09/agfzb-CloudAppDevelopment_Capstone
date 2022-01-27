function main(params) {

    secret = {
        "COUCH_URL": "https://f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY": "hhLIBg18IlcYe-ir_xf6aXAt3prqG4zNRjY_GDLAJwAH",
        "COUCH_USERNAME": "f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix"
    }

};

console.log(params);
return new Promise(function (resolve, reject) {
    const Cloudant = require('@cloudant/cloudant');
    const cloudant = Cloudant({
        url: secret.COUCH_URL,
        plugins: { iamauth: { iamApiKey: secret.IAM_API_KEY } }
    });
    const dealershipDb = cloudant.use('dealerships');

    if (params.state) {
        // return dealership with this state 
        dealershipDb.find({
            "selector": {
                "state": {
                    "$eq": params.state
                }
            }
        }, function (err, result) {
            if (err) {
                reject(err);
            }

            let code = 200;
            if (result.docs.length == 0) {
                code = 404;
            }
            resolve({
                statusCode: code,
                headers: { 'Content-Type': 'application/json' },
                body: result
            });
        });

    } else if (params.id) {
        id = parseInt(params.dealerId)
        // return dealership with this state 
        dealershipDb.find({ selector: { id: parseInt(params.id) } }, function (err, result) {
            if (err) {
                reject(err);
            }
            let code = 200;
            if (result.docs.length == 0) {
                code = 404;
            }

            resolve(
                {
                    statusCode: code,
                    headers: { 'Content-Type': 'application/json' },
                    body: result

                });

        });

    } else {

        // return all documents 

        dealershipDb.list({ include_docs: true }, function (err, result) {

            if (err) {
                reject(err);
            }

            resolve({
                statusCode: 200,
                headers: { 'Content-Type': 'application/json' },
                body: result
            });
        });
    }
});

