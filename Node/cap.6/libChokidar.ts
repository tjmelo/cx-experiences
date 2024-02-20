import { watch } from 'chokidar';

const watcher = watch('.', {
    ignored: /[\/\\]\./,
    persistent: true
});

const log = console.log.bind(console);

watcher
    .on('add', path => { log(`File ${path} has been added.`)})
    .on('unlink', path => { log(`File ${path} has been removed.`) })
    .on('addDir', path => { log(`Directory ${path} has been added.`) })
    .on('unlinkDir', path => { log(`Directory ${path} has been removed.`) })
    .on('error', error => { log(`Error happened ${error}.`) })
    .on('ready', () => { log(`Initial scan complete. Ready for changes.`) })
    .on('raw', (event, path, details) => { log(`Raw event info ${event} ${path} ${details}.`) });

watcher
    .on('change', (path, stats) => {
        stats && log(`File ${path} changed size to ${stats.size}`)
    })
