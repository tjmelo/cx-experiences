import { createClient } from 'redis';
import { createServer } from 'net';
import { config } from 'dotenv';

config();
const PORT = process.env.APP_PORT;

const server = createServer(conn => {
    console.log('Connected!');

    const clientRedis = createClient();

    clientRedis.on('error', error => console.error('Error: ' + error));

    clientRedis.select(6);

    conn.on('data', data => {
        console.log(data + ' from ' + conn.remoteAddress + ' ' + conn.remotePort);
        
        clientRedis.rPush('images', data);
    });
}).listen(PORT);

console.log(`Listening on port ${PORT}`);
