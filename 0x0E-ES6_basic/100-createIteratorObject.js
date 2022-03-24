export default function createIteratorObject(report) {
  return {
    * [Symbol.iterator]() {
      for (const employee of Object.values(report.allEmployees)) {
        for (const i of employee) yield i;
      }
    },
  };
}
