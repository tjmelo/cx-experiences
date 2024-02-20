import { writeFile, readFile } from "fs";

const pathToManipulateFile = './assets/files/writeFS/writeFile.txt';

writeFile(pathToManipulateFile, 'Writing in a file', (err) => {
    err && console.log(err);

    readFile(pathToManipulateFile, 'utf-8', (data, err) => {
        err && console.error(err);

        console.log(data);
    })
})
