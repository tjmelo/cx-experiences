import { Socket } from 'net';

const PORT = 3000;

const client = new Socket();
client.setEncoding('utf-8');

//server connect
client.connect(PORT, 'localhost', () => {
    console.log('Connected to server...');
    client.write('Who needs a browser to communicate?');
});

//get data, send to server
process.stdin.on('data', (data) => {
    client.write(data);
});

//when get the data, send us to console
client.on('data', (data) => {
    console.log(data);
});

//when the server closes the connection
client.on('close', () => {
    console.log('Connection is closed.')
})
