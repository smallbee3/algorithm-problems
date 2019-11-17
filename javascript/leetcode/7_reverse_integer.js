/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let sum = 0;
    let i = 0;
    let isMinus = null;

    if (x > (2 ** 31 - 1) || x < (-1 * 2 ** 31)) {
        return 0;
    }

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
