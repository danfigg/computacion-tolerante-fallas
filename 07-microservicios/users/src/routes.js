import express from 'express';
import { pool } from './db.js';

const router = express.Router();

// Crear usuario
router.post('/register', async (req, res) => {
  const { name, email, phone } = req.body;
  try {
    const [result] = await pool.query(
      'INSERT INTO users (name, email, phone) VALUES (?, ?, ?)',
      [name, email, phone]
    );
    res.status(201).json({ id: result.insertId });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// Obtener todos los usuarios
router.get('/', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM users');
    res.json(rows);
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// Obtener un usuario por ID
router.get('/:id', async (req, res) => {
  const { id } = req.params;
  try {
    const [rows] = await pool.query('SELECT * FROM users WHERE id = ?', [id]);
    if (rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(rows[0]);
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// Actualizar un usuario
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const { name, email, phone } = req.body;
  try {
    const [result] = await pool.query(
      'UPDATE users SET name = ?, email = ?, phone = ? WHERE id = ?',
      [name, email, phone, id]
    );
    if (result.affectedRows === 0) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json({ message: 'User updated' });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// Eliminar un usuario
router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  try {
    const [result] = await pool.query('DELETE FROM users WHERE id = ?', [id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json({ message: 'User deleted' });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

export default router;
