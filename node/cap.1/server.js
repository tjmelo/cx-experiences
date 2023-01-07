import { createServer } from 'http'
import { log } from '../assets/log.mjs'

const server = (req, res) => {
    res.writeHead(200, {'ContentType': 'text/plain'})
    res.end('Hello Word!!')
}

createServer(server).listen(3000)

log()