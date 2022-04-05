export default function updateStudentGradeByCity(list, city, newGrades) {
  return list.filter(
    (student) => student.location === city,
  ).map(
    (student) => newGrades.filter((grade) => grade.id === student.id),
  );
}
