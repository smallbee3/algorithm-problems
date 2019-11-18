/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {    
    function findLength(value) {
        let count = 0;
        const store = {}
        for (let i of value) {
            if (store[i]) {
                break;
            }
            store[i] = 1;
            count++;
        }
        return count;
    }

    let longest = 0;
    for (let i = 0; i < s.length; i++) {
        let result = findLength(s.slice(i))
        if (result > longest) {
            longest = result
        }
    }
    return longest;
};


result = lengthOfLongestSubstring("abcabcbb")
// result = lengthOfLongestSubstring("bbbbb")
// result = lengthOfLongestSubstring("pwwkew")
console.log(result)
