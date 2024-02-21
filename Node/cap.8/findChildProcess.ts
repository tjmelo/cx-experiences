import { spawn } from 'child_process';

const findProcess = spawn('find', ['.', '-ls']);
const grepProcess = spawn('grep', ['test']);

grepProcess.stdout.setEncoding('utf-8');

findProcess.stdout.pipe(grepProcess.stdin);

grepProcess.stdout.on('data', data => console.log(data));

findProcess.stderr.on('data', data => console.log('grep process strerr: ' + data));

findProcess.on('close', code => code !== 0 && console.log('Find process exited with code ' + code ));

grepProcess.on('exit', code => code !== 0 && console.log('Grep process exited with code ' + code));
