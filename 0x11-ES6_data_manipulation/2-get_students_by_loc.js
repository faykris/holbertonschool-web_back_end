export default function getStudentsByLocation(list, city) {
  return typeof list === 'object' ? list.filter((student) => student.location === city) : [];
}
