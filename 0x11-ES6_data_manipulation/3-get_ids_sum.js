export default function getStudentIdsSum(arg) {
  return arg.reduce((accumulator, currentValue) => accumulator + currentValue.id, 0);
}
