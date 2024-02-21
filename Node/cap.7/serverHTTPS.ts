import { readFileSync } from 'fs';
import { createServer } from 'https';

const STATUS = 200;
const PORT = 3000

const serverPrivateKey = readFileSync('./cert/site.key').toString();
const serverCertificate = readFileSync('./cert/final.crt').toString();

const options = {
    key: serverPrivateKey,
    cert: serverCertificate
};

createServer(options, (request, response) => {
    response.writeHead(STATUS);
    response.end('Hello Secure World!\n');
}).listen(PORT)
