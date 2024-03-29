Experiences by Framework Node.js
=
> All the code snippets are experienced by tests in applications.


<hr />

<br />

<div align="center">
  <img width="250" src="assets/img/logo-node.png">
</div>

### Requirements 
![Node.js](https://img.shields.io/badge/Node.js-gray?style=flat&logo=Node.js)
![NPM](https://img.shields.io/badge/npm-gray?style=flat&logo=Npm)

The code snippets were created by using node version: `v16+` 

Instructions
=

Download the project and install the necessary dependencies

```console
cx@experiences:~$ npm install
```

### Note
For security questions, all information about the port and status code was allocated inside a `.env`. So, it's necessary to create a new file `.env` at the root of the application, as below:

```bash
APP_PORT=3000 #port example
STATUS_CODE=200 #status code example
```

## Chapters' run references

<details>
  <summary>References Chapter 1</summary>
  <hr />
  <strong>Creating a trivial server</strong>
  <br />
  <code>npm run cap1:server</code>
  <hr />
  <strong>Creating a personal Hello World</strong>
  <br />
  <code>npm run cap1:hello</code>

  _Example with conditional URL. Type: http://localhost:3000/?name=node_
  <hr>
</details>

<details>
  <summary>References Chapter 2</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:buffers</code><br />
  <code>npm run start:eventEmitter</code><br />
  <code>npm run start:eventEmitterInherits</code><br />
  <code>npm run start:getChangeDataByFile</code><br />
  <code>npm run start:timers</code><br />
  <code>npm run start:stdin</code><br />
  <code>npm run start:server2</code>
  <hr>
</details>

<details>
  <summary>References Chapter 3</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:require</code><br />
  <code>npm run start:async</code><br />
  <code>npm run start:sandbox</code><br />
  <hr />
</details>

<details>
  <summary>References Chapter 4</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:repl</code><br />
  <hr>
</details>

<details>
  <summary>References Chapter 5</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:server3</code><br />
  <code>npm run start:staticServer</code><br />
  <code>npm run start:queryStringParser</code><br />
  <code>npm run start:getServerPost</code><br />
  <code>npm run start:getClientPost</code><br />
  <hr>
</details>

<details>
  <summary>References Chapter 6</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:libChokidar</code><br />
  <code>npm run start:libZlib</code><br />
  <code>npm run start:moduleOS</code><br />
  <code>npm run start:moduleReadLline</code><br />
  <code>npm run start:readDir</code><br />
  <code>npm run start:writeAtFile</code>
  <hr />
</details>

<details>
  <summary>References Chapter 7</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:clientTCP</code><br />
  <code>npm run start:clientUDP</code><br />
  <code>npm run start:serverHTTPS</code><br />
  <code>npm run start:serverTCP</code><br />
  <code>npm run start:serverUDP</code>
  <hr />
</details>

<details>
  <summary>References Chapter 8</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:childProcess</code><br />
  <code>npm run start:findChildProcess</code><br />
  <code>npm run start:findChildProcessWithoutBuffer</code><br />
  <hr />
</details>

<details>
  <summary>References Chapter 9</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:promisifying</code><br />
  <code>npm run start:promisifyingWithWrite</code>
  <hr />
</details>

<details>
  <summary>References Chapter 10</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run start:simpleExpressRequest</code><br />
  <code>npm run start:serverWithRedis</code><br />
  <code>npm run start:messageWithRedis</code><br />
  <p>There's an complete example of an application generated by <b>express generator</b>. <a href="/Node/cap.10/completeExpressAppReference/">See here</a>.</p>
  <hr />
</details>

<details>
  <summary>References Chapter 11</summary>
  <hr />
  <strong>Commands run and test:</strong>
  <br />
  <code>npm run test:simpleNodeUnitTest</code><br />
  <code>npm run test:simpleAssertFailTest</code><br />
  <code>npm run test:simpleNodeUnitTest</code><br />
  <code>npm run test:simpleMochaTest</code><br />
  <code>npm run test:loadtest</code><br />
  <hr />
</details>

<details>
  <summary><b>Load Test</b></summary>
  <hr />
  <strong>Start an app server</strong>
  <br />
  <code>npm run cap1:server</code>
  <br />
  <strong>Load test for server</strong>
  <br />
  <code>npm run test:loadtest</code>
</details>

