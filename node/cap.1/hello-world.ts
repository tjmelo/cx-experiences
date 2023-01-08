import { createServer } from "http";
import { parse } from 'url';
import { readFileSync, stat } from "fs";
import { log } from '../assets/log';

const queryString = (query, req, res) => {
    query === undefined && (query = 'world =]')
    
    if(query === 'node') {
        let file = 'assets/img/logo-node.png'
        stat(file, (err, stat) => {
            if(err) {
                console.error(err);
                res.writeHead(200, { 'Content-Type': 'text/plain' })
                res.end('Sorry, the Node JS isn\'t around here')
            } else {
                let img = readFileSync(file);
                res.contentType = 'image/png';
                res.conentLength = stat.size;
                res.end(img, 'binary');
            }
        })
    } else {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`Hello ${query} \n`)
    }
}

const server = (req, res) => {
    let name = parse(req.url, true).query.name;
    queryString(name, req, res);
}

createServer(server).listen(3000)

log()