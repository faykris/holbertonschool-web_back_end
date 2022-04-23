import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { AssertionError } from 'chai';

const queue = kue.createQueue();
const expect = require("chai").expect;

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
];

describe('createPushNotificationsJobs', function () {

  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array passing Number', function () {
    expect(function () {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', function () {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    });
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql({
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account',
    });
  });

  it('display an Asestion error when queue is undefined', function () {
    expect(function () {
      createPushNotificationsJobs(jobs, undefined);
    }).to.throw(AssertionError());
  });

  it('display a undefined value if jobs is an empty array', () => {
    const value = createPushNotificationsJobs([], queue);
    expect(value).to.equal(undefined);
  });

});
