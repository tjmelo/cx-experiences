import express from 'express';
import { config } from 'dotenv'

config();

const app = express();
const PORT = process.env.APP_PORT;

app.get('/', (req, res) => res.send('Hello World with express...'));

app.listen(PORT, () => console.log(`Example app listening on port: ${PORT}`));
