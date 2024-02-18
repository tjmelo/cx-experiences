import { createServer } from "http";
import { parse } from 'querystring';
import { log } from "../assets/log";

const PORT: string = process.env.APP_PORT;
const STATUS: number|any = process.env.STATUS_CODE;

const server = createServer().listen(PORT);

server.on('request', (req, res) => {

    if(req.method.includes('POST')) {
        let dataBody = '';

        req.on('data', (data) => {
            dataBody += data;
        });

        req.on('end', () => {
            const dataPost = parse(dataBody);
            console.log(dataPost);

            res.writeHead(STATUS, {'Content-Type': 'text/plain'});
            res.end('Hello World!');
        });
    }
})

log()
