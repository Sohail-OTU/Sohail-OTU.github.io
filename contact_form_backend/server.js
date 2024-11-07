// server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// MongoDB Connection
mongoose.connect('mongodb+srv://sohailbaig:LIT3msDSPBsmTih6@cluster0.3qlql.mongodb.net/', {})
    .then(() => console.log('MongoDB connected'))
    .catch((err) => console.log('Error:', err));

// Schema for Contact Form Data
const ContactSchema = new mongoose.Schema({
  first_name: String,
  last_name: String,
  email_: String,
  phone_: String,
  comments_: String,
});

const Contact = mongoose.model('Contact', ContactSchema);

// POST Route to handle form submissions
app.post('/submit', async (req, res) => {
  try {
    const contactData = new Contact(req.body);
    await contactData.save();
    res.status(200).send('Form submission successful!');
  } catch (error) {
    res.status(500).send('Error submitting form');
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
