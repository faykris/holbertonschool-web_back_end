import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

subscriber.on('message', function (channel, message) {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    process.exit(0);
  }
});

subscriber.subscribe('holberton school channel');
