export default function getStudentsByLocation(students, city) {
  return students.filter((citys) => citys.location === city);
}
