"use strict";

console.log('Loading function');

const aws = require('aws-sdk');

const s3 = new aws.S3({ apiVersion: '2006-03-01' });


exports.handler = (event, context, callback) => {
    console.log('Received event:', JSON.stringify(event, null, 2));

    // Get the object from the event and show its content type
    const bucket = event.Records[0].s3.bucket.name;
    const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
    const params = {
        Bucket: bucket,
        Key: key,
    };
    
    // Added Logics, --Max, 2016-12-19
    let max = 100000;
    let min = 0;
    let rnum = Math.floor(Math.random()*max + min);
    function prefix_integer(num, length) {
        return (Array(length).join('0') + num).slice(-length);
    }
    let snum = prefix_integer(rnum, 5) 
    console.log ("generated random number is " + snum);
    
    s3.getObject(params, (err, data) => {
        if (err) {
            console.log(err);
            const message = `Error getting object ${key} from bucket ${bucket}. Make sure they exist and your bucket is in the same region as this function.`;
            console.log(message);
            callback(message);
        } else {
            console.log('CONTENT TYPE:', data.ContentType);
            callback(null, data.ContentType);
        }
    });
    

};

