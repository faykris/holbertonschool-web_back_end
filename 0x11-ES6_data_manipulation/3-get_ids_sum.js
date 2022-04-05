export default function getStudentIdsSum(array) {
  const initialValue = 0;
  return array.reduce(
    (previousValue, currentValue) => previousValue + currentValue.id,
    initialValue,
  );
}
