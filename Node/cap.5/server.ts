import { createServer } from 'http'
import { log } from '../assets/log';

const PORT: string = process.env.APP_PORT;
const STATUS: number|any = process.env.STATUS_CODE;

const server = createServer().listen(PORT);

server.on('request', (req, res) => {
    console.log(req.method)

    res.writeHead(STATUS, {'Content-Type': 'text/plain'});
    res.end('Hello World!');
})

log()
