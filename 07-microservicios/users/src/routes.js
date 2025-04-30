import express from 'express';
import { pool } from './db.js';

const router = express.Router();

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

router.get('/', async (req, res) => {
  const [rows] = await pool.query('SELECT * FROM users');
  res.json(rows);
});

export default router;
