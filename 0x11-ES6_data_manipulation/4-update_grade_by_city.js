export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const studentByCity = students.filter((x) => x.location === city);
  const result = studentByCity.map((x) => {
    const grade = newGrades.filter((y) => y.studentId === x.id)
      .map((z) => z.grade)[0] || 'N/A';
    return { ...x, grade };
  });
  return result;
}
