/* eslint-env es6 */
/* eslint-disable no-console */
const express = require("express");
const bodyParser = require("body-parser");
const {spawn} = require('child_process');
const app = express();
const fs = require("fs");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
 res.sendFile(`${__dirname}/public/index.html`);
});

app.post("/readPython", (request, response) => {
      var dataToSend;
      const python = spawn('python3', ['public/Model.py']);

     python.stdout.on('data', function (data) {
      dataToSend = data.toString();
     });

     python.stderr.on('data', data => {
      console.error(`stderr: ${data}`);
     });

     python.on('exit', (code) => {
     console.log(`child process exited with code ${code}, ${dataToSend}`);
     response.sendFile(`${__dirname}/public/index.html`);
    }); 
});