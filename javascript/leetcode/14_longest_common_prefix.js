// /**
//  * @param {string[]} strs
//  * @return {string}
//  */


// 1) Bubbling

var longestCommonPrefix = function(strs) {
    // 1)
    let longest = strs[0];
    for (let string of strs.slice(1)) {

        const short = longest.length < string.length ? longest : string;
        let common_str = '';

        for (let i = 0; i < short.length; i++) {
            if (longest[i] == string[i]) {
                common_str += longest[i];
            }
            else {
                // longest = common_str;
                break;
            }
        }
        longest = common_str;
    }
    return longest ? longest : '';
}


// 2) Bubbling (Separation)
// var longestCommonPrefix = function(strs) {
//     function findCommonPrefix(a, b) {
//         let commonPrefix = '';
//         const shorterLength = a.length < b.length ? a.length : b.length;
//         for (let i = 0; i < shorterLength; i++) {
//             if (a[i] == b[i]) {
//                 commonPrefix += a[i];
//             }
//             else {
//                 break;
//             }
//         }
//         return commonPrefix
//     }
//     start = strs[0];
//     for (let i of strs.slice(1)) {
//         start = findCommonPrefix(start, i)
//     }
//     return start ? start : ''
// };

result = longestCommonPrefix(['abc'])
// result = longestCommonPrefix([])
// result = longestCommonPrefix(["aca","cba"])
// result = longestCommonPrefix(["aa","a"])
console.log(result)


// 200425
// 3) Bubbling (timeout) < 1) Bubbling is more simple

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    // let shortest = 0;
    // for (let str of strs) {
    //     if (str.length < shortest) {
    //         shortest = str.length;
    //     }
    // }

    let commonStr = strs.length > 0 ? strs[0] : '';
    for (let i = 1; i < strs.length; i++) {
        console.log(i, commonStr, strs[i]);
        for (let j = 0; j < commonStr.length; j++) {
            if (commonStr[j] !== strs[i][j]) {
                commonStr = commonStr.slice(0, j);
            }
        }
    }
    console.log(commonStr)
    return commonStr
};

// longestCommonPrefix(["flower","flow","flight"])
longestCommonPrefix(["dog","racecar","car"])
// longestCommonPrefix([])