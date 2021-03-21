/**
 * @param {string[]} strs
 * @return {string}
 */

// from 19:07pm
// to 19:43pm

// Runtime: 116 ms, faster than 9.09%
// Memory Usage: 43.2 MB, less than 5.34%

const longestBetweenTwo = (str1, str2) => {
  let longest = '';
  let loopNum = str1.length < str2.length ? str1.length : str2.length;
  for (let i = 0; i < loopNum; i++) {
    if (str1[i] === str2[i]) {
      longest += str1[i];
    } else {
      break;
    }
  }
  return longest;
};

var longestCommonPrefix = function (strs) {
  if (strs.length === 0) return '';

  let longest = strs[0];
  for (const str of strs.slice(1)) {
    const result = longestBetweenTwo(longest, str);
    console.log({ result });
    longest = result.length < longest.length ? result : longest;
  }

  return longest;
};

// const result = longestCommonPrefix(['flower', 'flow', 'flight']);
// const result = longestCommonPrefix(['dog', 'racecar', 'car']);
// const result = longestCommonPrefix(['dog', 'dgdgddog', 'dog']);
const result = longestCommonPrefix([]);

console.log(result);
