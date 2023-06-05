var express = require('express');
var fs = require('fs');

var app = express();


var accountInfo = {
    "admin_test_account": {
        "pass": "test123"
    },
    "admin": {
        //users are suppossed to reset the pass to login this account
        "pass": "gAX05BP9lmVWye3U9KmoP9kTX47ja1PlaZFiNlEOHbQqqRXeka"
    }
}

host = '0.0.0.0'
app.listen(8080, host);

app.get("/post_text/:id", function (req, res) {
    var id = req.params.id;

    if (id == "RT2RgPWHv8QXt0V") {
        res.send("<p>To solve the code, find three pieces of it and piece them together (in order). To start off, \
        Piece 2: DISM_DCDF_ROCKS</p><a href=\"/\">Go Back</a>");
    } else if (id == "SdffpYwmY0HMG9T") {
        res.send("<p>I like cats! So, here are some fun questions for you to try. See if you can answer any of them!</p>\
        <p>1. Cats are part of the _____ family? (starts with \'f\')</p>\
        <p>2. What is a female cat called? _____ (starts with \'m\')</p>\
        <p>3. Wild cats are known as _____ cats? (starts with \'f\')</p>\
        <p>Put them together, capitalised, separated by underscore, get Piece 3!</p>\
        <p>Example: If ans for 1 is \'ab c\', 2 is \'cat\', piece will be \'AB_C_CAT\'</p>");
    } else if (id == "Hh6XaG680uDEZH5") {
        res.send("<p>Welcome! This blog is all about my experiences with many things, like what is happening in my life. \
        To start it off, I want to show you some of the work I did when creating this blog. It was so much hard work designing \
        the web pages! I will be showing you the cool stuff I did to complete this page!</p>\
        <p>First, I made sure to choose the right navigation bar. The effects and layout were tough though! At last, I have \
        made a really cool navigation bar that just looks quite nice!</p>\
        <img src=\"/images/nav_bar_design.png\">\
        <p>Wow! After designing the web page, it is time to configure the server to work! This is such tough work, as I have \
        to test and ensure all the pages load correctly! Anyways, here are some configurations I did to server (so tired after \
        writing this). I hope you enjoy</p>\
        <img src=\"/images/fake_terminal.png\">\
        <p>* note: above is a fake terminal that has no functionality in whatever systems. It is to demonstrate for the CTF \
        challenge only</p>");
    } else {
        res.send("invalid request");
    }
});

app.get("/", function (req, res) {

    var u_input = req.query.user;
    var p_input = req.query.pass;
    if (u_input != undefined && p_input != undefined) {
        if (u_input == "admin_test_account" && p_input == accountInfo["admin_test_account"]["pass"]) {
            //completed a challenge, redirect to admin panel to reset password
            res.redirect("/admin");
        } else if (u_input == "admin" && p_input == accountInfo["admin"]["pass"]) {
            //completed all login challenge
            res.send("login challenge complete. Piece 1: WOW_OMG")
        } else {
            res.send("<p>Wrong username/password. Try again</p><a href=\"/\">Go Back</a>");
        }
    } else {
        //normal access
        var content = fs.readFileSync("./public/index.html", "utf-8");
        res.status(200);
        res.send(content);
    } 
});

app.get("/verify", function (req, res) {
    var pieces_combined = req.query.complete_piece
    if (pieces_combined == "WOW_OMGDISM_DCDF_ROCKSFELIDAE_MOLLY_FERAL") {
        res.send("CONGRATULATIONS! CHALLENGE SOLVED! FLAG: YCEP2023{DISM_DCDF_FOREVER}");
    } else {
        res.send("<p>Sorry, please try again!</p><a href=\"/\">Go Back</a>");
    }
})

app.get("/admin", function (req, res) {
    var newPass = req.query.pass
    if (newPass == undefined) {
        //only load the page
        var content = fs.readFileSync("./public/admin.html", "utf-8");
        res.status(200);
        res.send(content);
    } else {
        accountInfo["admin"]["pass"] = newPass;
        res.status(200);
        res.send("<p>Password for \'admin\' updated successfully! Use this password to login next time: " + newPass + "</p><a href=\"/\">Go Back</a>");
    }
})

app.get("/:contentToRead", function (req, res) {
    var contentToRead = req.params.contentToRead

    fs.readFile("./public/" + contentToRead + ".html", "utf-8", function (err, contents) {
        if (err) {
            res.status(404);
            res.send("404 Not Found")
        } else {
            res.status(200);
            res.send(contents);
        }
    });
});

app.get("/images/:contentToRead", function (req, res) {
    var contentToRead = req.params.contentToRead

    res.status(200);
    res.type('png');
    res.sendFile(__dirname + "/public/images/" + contentToRead);
});