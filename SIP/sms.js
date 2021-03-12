// Was interested in spam calls, so decided to find out how its done

const accountSid = process.env.; // SECRETS
const authToken = process.env.; // SECRETS
const client = require('twilio')(accountSid, authToken);

client.messages
  .create({
     body: 'Simple SMS',
     from: '+000000000',
     to: '+000000000'
   })
  .then(message => console.log(message.sid));
