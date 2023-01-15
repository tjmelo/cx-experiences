import { createServer } from "http";
import { log } from "../assets/log";

const server = createServer()

server.on('request', (req, res) => {
    console.log(`----------------------\n Request event..`)
    res.writeHead(200, {'Content-Type': 'text/plain'})
    res.end(`Hello application event...\n`)
})

server.on('connection', (req, res) => {
    console.log(`----------------------\n Connection server...`)
})

server.listen(process.env.APP_PORT, () => {
    console.log(`---------------------- \n Listening events...`)
})

log()