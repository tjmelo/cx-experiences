import { createServer } from 'http';
import { createReadStream, stat } from 'fs';
import { normalize } from 'path';

import { log } from '../assets/log';

createServer((request, response) => {
    const pathName = normalize(`${__dirname}/template/${request.url}`);

    stat(pathName, (error, stats) => {
        if(error) {
            console.error(error);
        
            response.writeHead(404);
            response.write('Resource missing 404\n');
            response.end();
        } else {
            response.setHeader('Content-Type', 'text/html');
        
            const file = createReadStream(pathName);

            file.on('open', () => {
                response.statusCode = Number(process.env.STATUS_CODE);
                file.pipe(response);
            });

            file.on('error', (error) => {
                console.error(error);

                response.writeHead(403);
                response.write('File missing or permission problem');
                response.end();
            })
        }
    })

}).listen(process.env.APP_PORT);

log()
