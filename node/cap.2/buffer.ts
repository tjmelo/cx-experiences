// Creating a new Buffer..

const str = 'Some string';
const buf = Buffer.from(str);

console.log('Buffer ->', buf)

const encodedData = JSON.stringify(buf);

console.log('Encoded Buffer ->', encodedData)

// Reading encoded data..

const decodedBuffer = Buffer.from(JSON.parse(encodedData).data)
console.log('Decoded Buffer ->', decodedBuffer.toString())
