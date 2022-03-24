export default function createIteratorObject(report) {
  let iterable = [];

  iterable = {
    * [Symbol.iterator]() {
      for (const employee of Object.values(report.allEmployees)) {
        for (const i of employee) yield i;
      }
    },
  };

  return iterable;
}
