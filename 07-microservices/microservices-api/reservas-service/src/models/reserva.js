// src/models/reserva.js
const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Reserva = sequelize.define('Reserva', {
  servicio: {
    type: DataTypes.ENUM('corte', 'disenio_barba', 'afeitado'),
    allowNull: false
  },
  fecha: {
    type: DataTypes.DATEONLY,
    allowNull: false
  },
  hora: {
    type: DataTypes.TIME,
    allowNull: false
  }
});

module.exports = Reserva;
