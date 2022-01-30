// server.js where your app starts

// init project
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
      // Reading Python files
      var dataToSend;
      // spawn new child process to call the python script
      const python = spawn('python3', ['public/script.py', "hi", "Duyen"]);

     // collect data from script
     python.stdout.on('data', function (data) {
      dataToSend = data.toString();
     });

     python.stderr.on('data', data => {
      console.error(`stderr: ${data}`);
     });

     // in close event we are sure that stream from child process is closed
     python.on('exit', (code) => {
     console.log(`child process exited with code ${code}, ${dataToSend}`);
     response.sendFile(`${__dirname}/public/result.html`);
    }); 
});

// listen for requests :)
var listener = app.listen(process.env.PORT, () => {
  console.log(`Your app is listening on port ${listener.address().port}`);
});
