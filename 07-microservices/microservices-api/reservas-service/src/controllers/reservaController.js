const Reserva = require('../models/reserva');

// Crear
exports.createReserva = async (req, res) => {
  try {
    const { servicio, fecha, hora } = req.body;
    const reserva = await Reserva.create({ servicio, fecha, hora });
    res.status(201).json(reserva);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Leer todas
exports.getReservas = async (req, res) => {
  try {
    const reservas = await Reserva.findAll();
    res.json(reservas);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Leer una
exports.getReservaById = async (req, res) => {
  try {
    const reserva = await Reserva.findByPk(req.params.id);
    if (!reserva) return res.status(404).json({ error: 'Reserva no encontrada' });
    res.json(reserva);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Actualizar
exports.updateReserva = async (req, res) => {
  try {
    const { servicio, fecha, hora } = req.body;
    const [updated] = await Reserva.update({ servicio, fecha, hora }, {
      where: { id: req.params.id }
    });
    if (!updated) return res.status(404).json({ error: 'Reserva no encontrada' });
    const updatedReserva = await Reserva.findByPk(req.params.id);
    res.json(updatedReserva);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Eliminar
exports.deleteReserva = async (req, res) => {
  try {
    const deleted = await Reserva.destroy({ where: { id: req.params.id } });
    if (!deleted) return res.status(404).json({ error: 'Reserva no encontrada' });
    res.json({ message: 'Reserva eliminada' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
