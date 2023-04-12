const timer1 = setTimeout((name) => {
    console.log(`Running timeout ${name}`)
}, 3000, 'TIMEOUT');

const timer2 = setInterval((name) => {
    console.log(`Running interval ${name}`)
}, 5000, 'INTERVAL')

setTimeout(() => {
    console.log('Stopping interval...')
    // Stop interval immediately..
    timer2.unref()

    // Wait for program running
    // timer2.ref()

}, 12000)

console.log('Running program...')