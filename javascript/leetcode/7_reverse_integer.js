
// 1)
// 76 ms	36.5 MB

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let sum = 0;
    let i = 0;
    let isMinus = null;

    if (x < 0) {
        isMinus = true;
        x = x * -1;
    }
    for (let num of x.toString()) {
        sum = sum + num * 10 ** i;
        i++;
    }
    const result = isMinus ? -1 * sum : sum;

    if (result > (2 ** 31 - 1) || result < (-1 * 2 ** 31)) {
        return 0;
    }
    return result;
};

result = reverse(1534236469);
console.log(result);



// 2) 
// 88 ms	37.9 MB

/**
 * @param {number} x
 * @return {number}
 */

var reverse = function(num) {
    if (num > 2**31-1 || num < 2**31*-1) {
        return 0;
    }

    let isMinus = false;
    if (num < 0) {
        num = num * -1
        isMinus = true;
    }

    let numStr = String(num);
    let reverseNumStr = ''
    for (let i = 0; i < numStr.length; i++) {
        reverseNumStr = String(numStr[i]) + reverseNumStr;
    }

    num = Number(reverseNumStr);
    num = isMinus ? num * -1 : num;

    if (num > 2**31-1 || num < 2**31*-1) {
        return 0;
    }

    console.log(num);
    return num
};

reverse(123);
reverse(-123);
reverse(120);
reverse(1534236469);
