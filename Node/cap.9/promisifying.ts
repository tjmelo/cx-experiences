import { readFile } from 'fs/promises';

readFile('./assets/files/apples.txt')
    .then(data => console.log(data.toString()))
    .catch(error => console.error(error));
