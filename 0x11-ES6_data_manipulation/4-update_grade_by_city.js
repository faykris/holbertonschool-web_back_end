export default function updateStudentGradeByCity(list, city, newGrades) {
  return list.filter(
    (student) => student.location === city,
  ).map(
    (student) => {
      const std = student;
      const grades = newGrades.filter((grade) => grade.studentId === student.id);
      if (grades.length > 0) {
        std.grade = grades[0].grade;
      } else {
        std.grade = 'N/A';
      }
      return student;
    },
  );
}
