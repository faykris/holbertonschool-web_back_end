export default function getStudentsByLocation(list, city) {
  return list.filter((student) => student.location === city);
}
