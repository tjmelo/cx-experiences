import { createServer } from 'net';

const PORT = 3000;

const server = createServer((conn) => {
    console.log('Connected...');

    conn.on('data', (data) => {
        console.log(`${data} from ${conn.remoteAddress} ${conn.remotePort}`);

        conn.write(`Repeating ${data}`);
    });

    conn.on('close', () => console.log('Client close connection...'));
}).listen(PORT);

server.on('listening', () => console.log(`Listing on port ${PORT}`));

server.on('error', (err) => {
    if(err.name == 'EADDRINUSE') {
        console.warn('Address in use, retrying...');
        
        setTimeout(() => {
            server.close();
            server.listen(PORT);
        }, 1000);
    } else {
        console.log(err);
    }
})
