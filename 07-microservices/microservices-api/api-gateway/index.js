const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const cors = require('cors'); // 👈 importar cors
require('dotenv').config();

const app = express();

app.use(cors({
  origin: 'http://localhost:3000', 
}));

const USERS_SERVICE = process.env.USERS_SERVICE_URL;
const RESERVAS_SERVICE = process.env.RESERVAS_SERVICE_URL;

// Proxy para /users
app.use('/users', createProxyMiddleware({
  target: USERS_SERVICE,
  changeOrigin: true,
  pathRewrite: { '^/users': '/users' }
}));

// Proxy para /reservas
app.use('/reservas', createProxyMiddleware({
  target: RESERVAS_SERVICE,
  changeOrigin: true,
  pathRewrite: { '^/reservas': '/reservas' }
}));

const PORT = process.env.PORT || 4002;
app.listen(PORT, () => {
  console.log(`API Gateway running at http://localhost:${PORT}`);
});
