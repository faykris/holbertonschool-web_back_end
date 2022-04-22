import redis from 'redis';

const publisher = redis.createClient();

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    if (message === 'KILL_SERVER') {
      publisher.publish('holberton school channel', `${message}`);
    }
    else {
      publisher.publish('holberton school channel', `About to send ${message}`);
    }
  }, time);
}

publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
