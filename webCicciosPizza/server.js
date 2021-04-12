const http = require("http");
const fs = require("fs");
const path = require('path');
const express = require("express");
const sound = require("sound-play");

let app = express();

app.use(express.static("public"));

let server = app.listen("3000", function(req, resp) {
    console.log("Server Connesso");
});

app.get("/", function(req, resp, next) {
    fs.readFile("./menuIniziale/menuIniziale.html", "utf-8", function(err, data) {
        resp.write(data);
        sound.play(__dirname + "/public/audio/colonnaSonora.mp3", 1);
        resp.end();
    });
});

app.get("/livello1", function(req, resp, next) {
    fs.readFile("./livello/lvl.html", "utf-8", function(err, data) {
        resp.write(data);
        resp.end();
    });
});

app.get("/livello2", function(req, resp, next) {
    resp.send("IL LIVELLO ARRIVERA' PRESTO");
    resp.end();
});

app.get("/livello3", function(req, resp, next) {
    resp.send("IL LIVELLO ARRIVERA' PRESTO");
    resp.end();
});

app.get("/livello4", function(req, resp, next) {
    resp.send("IL LIVELLO ARRIVERA' PRESTO");
    resp.end();
});

app.get("/livello5", function(req, resp, next) {
    resp.send("IL LIVELLO ARRIVERA' PRESTO");
    resp.end();
});

app.get("/tutorial", function(req, resp, next) {
    resp.send("IL TUTORIAL ARRIVERA' PRESTO");
    resp.end();
});

app.get("/giroPizza", function(req, resp, next) {
    resp.send("COMING SOON");
    resp.end();
});