import { createInterface } from 'readline';

const rl = createInterface(process.stdin, process.stdout);

rl.question('>> What is the meaning of life? ', (awswer) => {
    console.log('About the meaning of life, you said' + awswer);
    rl.setPrompt(">> ");
    rl.prompt();
});

const closeInteface = () => {
    rl.close();
    console.log('Leaving Readline');
}

rl.on('line', (cmd) => {
    if(cmd.trim() === '.leave') {
        closeInteface();
        return;
    }

    console.log('repeating command: ' + cmd);
    rl.prompt();
});

rl.on('close', () => closeInteface());

