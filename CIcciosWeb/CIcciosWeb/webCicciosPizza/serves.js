const http = require("http");
const fs = require("fs");
const express = require("express");

let app = express();

let server = app.listen("3000", function(req, resp) {
    console.log("Server Connesso");
});

app.get("/carriera", function(req, resp, next) {
    let lvl = fs.readFile("./livello/lvl.html");
    resp.sendFile(lvl); //pagina livello 1
});

app.get("/giroPizza", function(req, resp, next) {
    resp.send("COMING SOON");
});