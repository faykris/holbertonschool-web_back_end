export default function cleanSet(set, startString) {
  let text = '';
  const array = [];

  if (startString || startString.length > 0) {
    for (const element of set) {
      if (element && element.startsWith(startString)) {
        array.push(element.slice(startString.length));
      }
    }
    text = array.join('-');
  }
  return text;
}
