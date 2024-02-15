import { EventEmitter } from "events";
import { createWriteStream } from "fs";

export class InputChecker extends EventEmitter {
    name: string;
    writeStream: import("fs").WriteStream;

    constructor(name: string, file: string) {
        super()
        this.name = name;
        this.writeStream = createWriteStream(`./assets/files/${file}.txt`, {
            flags: 'a',
            encoding: 'utf-8',
            mode: 0o666
        })
    }

    check(input: string) {
        let command = input.trim().substring(0, 3);

        if (command == 'wr:' ) {
            this.emit('write', input.substring(3, input.length))
        } else if (command == 'en:') {
            this.emit('end')
        } else {
            this.emit('echo', input)
        }
    }
    
}

const ic = new InputChecker('APPLICATION: ', 'output');

ic.on('write', data => ic.writeStream.write(data, 'utf-8'))
ic.on('echo', data => process.stdout.write(`${ic.name} wrote ${data}`))
ic.on('end', () => process.exit())

process.stdin.setEncoding('utf-8')
process.stdin.on('readable', () => {
    const input = process.stdin.read();
    input !== null && ic.check(input)
})

console.log('Type something here...')