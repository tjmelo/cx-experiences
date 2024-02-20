import { mkdir, readFile, writeFile } from 'fs/promises';

const pathToFile = './assets/files/'; 

readFile(pathToFile + 'apples.txt', 'utf8')
    .then((data) => {
        const adjData = data.toString().replace(/[A/a]pple/g, 'orange');
        mkdir(pathToFile + 'fruits/');
        
        return adjData;
    })
    .then((data) => writeFile(pathToFile + 'fruits/orange.txt', data))
    .catch(error => console.error(error));
