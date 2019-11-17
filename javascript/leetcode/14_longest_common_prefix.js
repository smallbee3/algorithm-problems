/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {

    if (strs.length < 1) {
        return ''
    }

    let str_1 = strs[0];
    for (let str_2 of strs.slice(1)) {
        let common_str = '';
        const longer_len = str_1.length > str_2.length ? str_1.length : str_2.length;
        for (let i = 0; i < longer_len; i++) {
            if (str_1[i] == str_2[i]) {
                common_str += str_1[i];
                console.log(1, common_str)
            }
            else {
                str_1 = common_str;
                console.log(2, str_1)
                break;
            }
        }
    }
    return str_1
};