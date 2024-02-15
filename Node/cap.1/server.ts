import { createServer } from 'http'
import { log } from '../assets/log'

const server = (req, res) => {
    res.writeHead(process.env.STATUS_CODE, {'ContentType': 'text/plain'})
    res.end('Hello Word!!')
}

createServer(server).listen(process.env.APP_PORT)

log()