import { createContext, isContext, runInContext } from 'vm';
import { inspect } from 'util';

const sandbox = {
    count1: 1
};

createContext(sandbox);

isContext(sandbox) && console.log('Contextualized...');

// Get current context of application..
runInContext('count1++; counter=true;', sandbox, {
    filename: 'context.vm'
});

console.log(inspect(sandbox));
