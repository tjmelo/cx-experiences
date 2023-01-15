console.log(`Type something...`)

process.stdin.on('data', data => {
    data.toString().trim() === 'exit'
    ? process.exit(0)
    : process.stdout.write(`You typed: ${ data.toString() } \n`);
})