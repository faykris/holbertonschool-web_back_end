import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstname, lastname, filename) {
  const user = await signUpUser(firstname, lastname).then((res) => ({
    status: 'fulfilled',
    value: res,
  }));
  const photo = await uploadPhoto(filename).catch((err) => ({
    status: 'rejected',
    value: `${err.name}: ${err.message}`,
  }));

  return [user, photo];
}
