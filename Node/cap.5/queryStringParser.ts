import { createServer } from 'http';
import { parse } from 'querystring';

import { log } from '../assets/log';

createServer((request, response) => {
    console.log(parse(request.url))
    
    // String...
    // localhost:3000/?value1=valueone&value1=valueoneb&value2=valuetwo
    
    // Expected result...
    // {
    //     value1: ['valueone', 'valueoneb']
    //     value2: 'valueTwo'
    // }

}).listen(process.env.APP_PORT);

log()
