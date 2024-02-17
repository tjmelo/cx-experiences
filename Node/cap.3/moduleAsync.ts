import { readFile } from 'fs';
import parallel from 'async/parallel';

const DIR = './assets/files/async';

const data1 = (callback: any) => {
    readFile(`${DIR}/fruit1.txt`, 'utf8', (err, data) => {
        callback(err, data)
    })
}

const data2 = (callback: any) => {
    readFile(`${DIR}/fruit2.txt`, 'utf8', (err, data) => {
        callback(err, data)
    })
}

const data3 = (callback: any) => {
    readFile(`${DIR}/fruit3.txt`, 'utf8', (err, data) => {
        callback(err, data)
    })
}

parallel({
    data1: data1,
    data2: data2,
    data3: data3,
}, (err, result) => {
    err 
        ? console.error(err)
        : console.log(result)
    
})
