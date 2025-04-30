import express from 'express';
import dotenv from 'dotenv';
import router from './routes.js';

dotenv.config();
const app = express();
app.use(express.json());

app.use('/users', router);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Users service running on port ${PORT}`);
});
