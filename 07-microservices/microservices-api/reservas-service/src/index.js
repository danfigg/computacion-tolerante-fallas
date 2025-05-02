require('dotenv').config();
const express = require('express');
const app = express();
const sequelize = require('./config/database');
const userRoutes = require('./routes/reservas');

app.use(express.json());
app.use('/reservas', userRoutes);

const PORT = process.env.PORT || 4001;

sequelize.authenticate()
  .then(() => {
    console.log('Database connected');
    // Sincroniza (crea tablas si no existen)
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
