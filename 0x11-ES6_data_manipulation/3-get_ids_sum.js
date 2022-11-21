export default function getStudentIdsSum(arg) {
  const array1 = arg.map(({ id }) => id);
  const sum = 0;
  return array1.reduce((accumulator, currentValue) => accumulator + currentValue, sum);
}
