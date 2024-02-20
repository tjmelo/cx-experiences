import { createGzip } from 'zlib';
import { createReadStream, createWriteStream } from 'fs';

const gzip = createGzip();

const inp = createReadStream('./assets/img/logo-node.png');
const out = createWriteStream('./assets/img/logo-node.png.gz');

inp.pipe(gzip).pipe(out);
