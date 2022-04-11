import express from 'express';
import controllerRouting from './routes/index';

const app = express();

controllerRouting(app);

app.listen(1245);

export default app;
