
const Cloudant = require('@cloudant/cloudant'); 

async function main(params) { 

    secret={ 
    "COUCH_URL": "https://f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix.cloudantnosqldb.appdomain.cloud", 
    "IAM_API_KEY": "hhLIBg18IlcYe-ir_xf6aXAt3prqG4zNRjY_GDLAJwAH", 
    "COUCH_USERNAME": "f12b5d67-d718-4b5a-ab21-b00755ea589e-bluemix" 
    } 

const cloudant = Cloudant({ 
        url: secret.COUCH_URL, 
        plugins: { iamauth: { iamApiKey: secret.IAM_API_KEY } } 
    }); 

    let dbListPromise = await getDbs(cloudant); 
    return dbListPromise; 
} 

function getDbs(cloudant) { 
    return new Promise((resolve, reject) => { 
        let db = cloudant.use('dealerships'); 
        let result = db.list( {fields : ['id','city','state','st','address','zip','lat','long','short_name','full_name'],
        include_docs:true} ) 
            .then(result => { 
                resolve({ body: result}) 
            }) 
            .catch(err => { 
                reject({ err: err}); 
            }); 
    }); 
} 



