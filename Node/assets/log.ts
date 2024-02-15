import { config } from 'dotenv'
config()

export const log = () => {
    console.log('Server running...')
    console.log('\x1b[32m%s\x1b[0m',`http://localhost:${process.env.APP_PORT}`)
}
