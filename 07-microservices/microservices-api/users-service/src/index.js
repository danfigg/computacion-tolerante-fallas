require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();
const sequelize = require('./config/database');
const userRoutes = require('./routes/users');

app.use(cors({
  origin: 'http://localhost:3000',
}));

app.use(express.json());
app.use('/users', userRoutes);

const PORT = process.env.PORT || 4000;

sequelize.authenticate()
  .then(() => {
    console.log('Database connected');
    return sequelize.sync();
  })
  .then(() => {
    app.listen(PORT, () => {
      console.log(`Server running on http://localhost:${PORT}`);
    });
  })
  .catch(err => {
    console.error('Unable to connect to the database:', err);
  });
