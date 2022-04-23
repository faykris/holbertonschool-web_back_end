import redis from 'redis';
import { promisify } from 'util';
import express from 'express';
import kue from 'kue';

const queue = kue.createQueue();
const client = redis.createClient();
const GET_ASYNC = promisify(client.get).bind(client);
let reservation;


/********** REDIS **********/
function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  return await GET_ASYNC('available_seats');
}

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  reserveSeat(50);
  reservation = true;
});


/********* EXPRESS *********/
const app = express();

app.listen(1245);

app.get('/available_seats', async function (req, res) {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', function (req, res) {
  if (reservation === true) {
    const job = queue.create('reserve_seat', {})
      .save((err) => {
        if (err) {
          res.json({ status: 'Reservation failed' });
        } else {
          res.json({ status: 'Reservation in process' });
        }
      });

    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
  } else {
    res.json({ status: 'Reservation are blocked' });
  }
});

app.get('/process', async function (req, res) {
  queue.process('reserve_seat', async function (job, done) {
    let availableSeats = await getCurrentAvailableSeats();

    if (availableSeats <= 0) done(Error('Not enough seats available'));

    availableSeats = Number(availableSeats) - 1;

    reserveSeat(availableSeats);

    if (availableSeats <= 0) reservation = false;

    done();
  });
  res.json({ status: 'Queue processing' });
});
