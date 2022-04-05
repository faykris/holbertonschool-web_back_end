export default function getListStudentIds(array) {
  if (typeof array !== 'object') return [];
  return array.map((x) => x.id);
}
