//NOTE: AI HELPED ME IN THIS JAVASCRIPT
//I seeked the help of AI to setup a node.js server
//to collect the data from my form. This code is for that.
//I will mention if I use AI anywhere else.


const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware to parse URL-encoded data from the form
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files (HTML, CSS)
app.use(express.static(path.join(__dirname, 'public')));

app.post('/submit-form', (req, res) => {
    // Extract form data from the request body
    const { firstName, lastName, email, phone, comments } = req.body;

    // form data handling
    console.log(`Form data received:
        First Name: ${first_name}
        Last Name: ${last_name}
        Email: ${email_}
        Phone: ${phone_}
        Comments: ${comments_}`);

    // Send a response to the user
    res.send(`<h2>Thank you, ${first_name}! Your form has been submitted successfully.</h2>`);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
