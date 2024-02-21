import { spawn } from "child_process";

const listPsProcess = spawn('ps', ['ax']);
const grepListProcess = spawn('grep', ['--line-buffered', 'apache2']);

listPsProcess.stdout.pipe(grepListProcess.stdin);

listPsProcess.stderr.on('data', data => console.log('ps stderr: ' + data));

listPsProcess.on('close', code => code !== 0 && console.log('ps process exited with code ' + code))

grepListProcess.stdout.on('data', data => console.log('' + data));

grepListProcess.stderr.on('data', data => console.log('grep stderr: ' + data));

grepListProcess.on('close', code =>  code !== 0 && console.log('grep process exited with code ' + code));
