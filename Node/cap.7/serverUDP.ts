import { createSocket } from 'dgram';

const server = createSocket('udp4');
const PORT = 3000;

server.on('message', (msg, rinfo) => {
    console.log(`Message: ${msg} from ${rinfo.address}: ${rinfo.port}`);
})

server.bind(PORT);
