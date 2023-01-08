import { createServer } from 'http'
import { log } from '../assets/log'

const server = (req: any, res: any) => {
    res.writeHead(200, {'ContentType': 'text/plain'})
    res.end('Hello Word!!')
}

createServer(server).listen(3000)

log()