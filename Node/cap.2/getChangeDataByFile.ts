import { readFileSync, writeFileSync } from 'fs'

const toManipulateFileAndData = () => {
    const getReadFile = readFileSync('./assets/files/apples.txt', 'utf8');
    console.log(getReadFile.toString());
    
    const getReplaceFile = getReadFile.replace(/[A/a]pples/g, 'oranges');
    writeFileSync('./assets/files/oranges.txt', getReplaceFile);
}

try {
    toManipulateFileAndData();
} catch (e) {
    console.error(e)
}
