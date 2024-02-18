import { request } from 'http';
import { stringify } from 'querystring';

interface IOptions {
    hostname: string,
    port: number,
    method: string,
    headers: {}
}

const PORT: number = 3000;

const postData = stringify({
    'msg': 'Hello World!'
});

const options: IOptions = {
    hostname: 'localhost',
    port: PORT,
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencode',
        'Content-Length': postData.length,
    }
};

const req = request(options, (res) => {
    console.log(`STATUS: ${res.statusCode}`);
    console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
    res.setEncoding('utf8');

    req.on('data', (chunk) => {
        console.log(`BODY: ${chunk}`)
    });

    res.on('end', () => {
        console.log('No more data in respose');
    })
})

req.on('error', (error) => {
    console.log(`Problem with request: ${error.message}`);
})

req.write(postData);
req.end();
