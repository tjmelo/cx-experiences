import { spawn } from "child_process";

const pwd = spawn('pwd');

pwd.stdout.on('data', (data) => {
    console.log('stdout: ' + data);
});

pwd.stderr.on('data', (data) => {
    console.error('stderr: ' + data);
});

pwd.on('close', (code) => {
    console.log('Child process exited with code: ' + code);
});
