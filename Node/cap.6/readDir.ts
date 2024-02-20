"use strict";

import { readdir, unlink } from 'fs';
import { extname } from 'path';

readdir('./', (err, files) => {
    
    for (let file of files){
        console.log(file);

        if (extname(file) === '.gz') {
            unlink(`./${file}`, null)
        }
    }
})
