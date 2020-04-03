
// 1) hashmap
// 600 ms	87 MB

// /**
//  * @param {string} s
//  * @return {number}
//  */
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




// 2) Simpler than 1)
// 496 ms	41.9 MB

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let longest = 0;
    for (let i = 0; i < s.length; i++) {
        let store = [];
        for (const a of s.slice(i)) {
            if (store.indexOf(a) < 0) {
                store.push(a);
            }
            else {
                break;
            }
        }
        longest = longest > store.length ? longest : store.length;
    }
    console.log(longest);
    return longest;
};

lengthOfLongestSubstring('abcabcbb');
lengthOfLongestSubstring('bbbbb');
lengthOfLongestSubstring('pwwkew');
