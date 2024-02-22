import { createClient } from 'redis';
import { createServer } from 'http';

const serverMessage = createServer();
const PORT = 8124;

serverMessage.on('request', (request, response  ) => {
    if (request.url === '/favicon.ico') {
        response.writeHead(200, {'Content-Type': 'image/x-icon'});
        response.end();
        return;
    }

    const client = createClient();

    client.on('error', error => console.log('Error ' + error));

    client.select(6);

    //@ts-ignore
    client.lPop('images', (error: any, reply: string) => {
        if (error) {
            return console.error(error);
        }
        
        if (reply) {
            response.write(reply + '\n');
        } else {
            response.write('End of queue\n');
        }

        response.end();
    });

    client.quit();
});

serverMessage.listen(PORT);

console.log(`Listening on ${PORT}`);
