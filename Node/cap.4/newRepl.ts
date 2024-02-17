import { start, REPL_MODE_STRICT } from 'repl'

start({
    prompt: '> ',
    replMode: REPL_MODE_STRICT,
    ignoreUndefined: true
})
