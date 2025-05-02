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
    },
    user_id: {
      type: DataTypes.INTEGER.UNSIGNED,
      allowNull: false
    },
    codigo: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true
    }
  });

  module.exports = Reserva;