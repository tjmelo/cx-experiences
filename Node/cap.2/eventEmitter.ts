import { EventEmitter } from "events";

let counter = 0;
const LIMIT_COUNT = 10;

const emitter = new EventEmitter();

setInterval(() => {
    emitter.emit('timed', counter++)
}, 3000)

console.log(counter)

emitter.on('timed', (data) => 
    data <= LIMIT_COUNT 
    ? console.log(`timed ${data}`)
    : process.exit()
)
