/**
 * @param {number} x
 * @return {number}
 */

// from 18:36pm
// to 19:00pm

// Runtime: 96 ms, faster than 77.81%
// Memory Usage: 40.6 MB, less than 17.82%

var reverse = function (x) {
  let is_minus = false;

  if (x < -1 * 2 ** 31 || x > 2 ** 31 - 1) {
    return 0;
  }

  if (x < 0) {
    is_minus = true;
    x = x * -1;
  }
  const strX = String(x);

  let reversedX = 0;
  for (let i = 0; i < strX.length; i++) {
    reversedX += Number(strX[i]) * 10 ** i;
  }

  if (reversedX < -1 * 2 ** 31 || reversedX > 2 ** 31 - 1) {
    return 0;
  }

  return is_minus ? reversedX * -1 : reversedX;
};

const result = reverse(123);
// const result = reverse(-123);
// const result = reverse(120);
// const result = reverse(0);

console.log(result);
