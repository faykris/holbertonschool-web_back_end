export default function getListStudentIds(array) {
  return Array.isArray(array) ? array.map((x) => x.id) : [];
}
