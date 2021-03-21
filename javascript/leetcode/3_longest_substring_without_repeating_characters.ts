/**
 * @param {string} s
 * @return {number}
 */

// from 16:18pm
// to 16:43pm

// Runtime: 476 ms, faster than 14.14%
// Memory Usage: 45 MB, less than 35.17%

var lengthOfLongestSubstring = function (s) {
  const s_length = s.length;
  let longestNum = 0;

  for (let i = 0; i < s_length; i++) {
    if (i !== 0) s = s.substr(1);
    // console.log({ s });

    const unrepeatedArr = [];
    for (const cha of s) {
      if (unrepeatedArr.indexOf(cha) > -1) {
        break;
      }
      unrepeatedArr.push(cha);
    }
    longestNum =
      unrepeatedArr.length > longestNum ? unrepeatedArr.length : longestNum;
  }
  return longestNum;
};

// const s = "abcabcbb"
// const s = "bbbbb"
// const s = 'pwwkew';
const s = '';

const result = lengthOfLongestSubstring(s);

console.log(result);
