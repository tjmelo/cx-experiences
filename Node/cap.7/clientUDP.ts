import { createSocket } from 'dgram';

const client = createSocket('udp4');
const PORT = 3000;
const URL = 'examples.burningbird.net';

process.stdin.on('data', (data) => {
    console.log(data.toString('utf-8'));

    client.send(data, 0, data.length, PORT, URL, (err, bytes) => {
        err 
            ? console.error(`error: ${err}`)
            : console.log('Successful')
    } )
})
