import { readFile } from 'fs';

let firstTest = 10;
let secondTest = 'test';

for(let i = 0; i <= firstTest; i++) {
    debugger;
    secondTest+=i;
};

setTimeout(() => {
    debugger;
    firstTest = 1000;
    console.log(secondTest);
}, 1000);

readFile('./cap.11/log.txt', 'utf-8', (err, data) => {
    err && console.error(err);
    
    const arrayItems = ['apple', 'orange', 'strawberry'];
    const arrayItemsReference = arrayItems.concat(data)

    console.log(arrayItemsReference);
});
