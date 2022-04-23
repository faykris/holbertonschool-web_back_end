const kue = require('kue')
  , queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}).save();

job.on('complete', function (result) {
  console.log(`Notification job created: ${job.id}`);
}).on('failed', function (errorMessage) {
  console.log('Notification job failed')
});
