'use strict';

console.log('Loading lambda on_post_put');
const aws = require('aws-sdk');
const s3 = new aws.S3({apiVersion: '2006-03-01'});
var ses = new aws.SES();


exports.handler = (event, context, callback) =>
{
    // console.log('Received event:', JSON.stringify(event, null, 2));
    // Get the object from the event and show its content type
    const bucket = event.Records[0].s3.bucket.name;
    const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
    const s3_params = {
        Bucket: bucket,
        Key: key,
    };

    s3.getObject(s3_params, (err, data) => {
        if (err) {
            console.log(err);
            const message = `Error getting object ${key} from bucket ${bucket}. Make sure they exist and your bucket is in the same region as this function.`;
            console.log(message);
            callback(message);
        } else {
            console.log('CONTENT TYPE:', data.ContentType);

    //begin SES block, --Max
    var msg_params = {
        Destination: {
            /* required */
            ToAddresses: [
                'maxwunj@gmail.com',
                /* more items */
            ]
        },
        Message: {
            /* required */
            Body: {
                /* required */
                Text: {
                    Data: `Notification from AWS SES. You have a new uploaded MD file ${key} in ${bucket}`, /* required */
                    Charset: 'UTF-8'
                }
            },
            Subject: {
                /* required */
                Data: `New post added -- ${key}` , /* required */
                Charset: 'UTF-8'
            }
        },
        Source: 'Contact to Max Wu', /* required */
        ReplyToAddresses: [
            'maxwunj@msn.com',
            /* more items */
        ]
    };  /* msg_params */
    ses.sendEmail(msg_params,
        function (err, data) {
            if (err)
                console.log(err, err.stack); // an error occurred
            else
                console.log(data);           // successful response
        }
    );

    callback(null, data.ContentType);
}  /* if-else */
});
};