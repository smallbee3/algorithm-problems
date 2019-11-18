/**
 * @param {string[]} strs
 * @return {string}
 */
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
    return longest ? longest : ''


    // 2)
    // function findCommonPrefix(a, b) {
    //     let commonPrefix = '';
    //     const shorterLength = a.length < b.length ? a.length : b.length;
    //     for (let i = 0; i < shorterLength; i++) {
    //         if (a[i] == b[i]) {
    //             commonPrefix += a[i];
    //         }
    //         else {
    //             break;
    //         }
    //     }
    //     return commonPrefix
    // }
    // start = strs[0];
    // for (let i of strs.slice(1)) {
    //     start = findCommonPrefix(start, i)
    // }
    // return start ? start : ''
};

// result = longestCommonPrefix(['abc'])
// result = longestCommonPrefix([])
// result = longestCommonPrefix(["aca","cba"])
result = longestCommonPrefix(["aa","a"])
console.log(result)