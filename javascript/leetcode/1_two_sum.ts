/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Runtime: 84 ms, faster than 38.53%
// Memory Usage: 40.6 MB, less than 10.98%

var twoSum = function (nums, target) {
  // const numsUnderTarget = nums.filter(num => num < target);

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    console.log('idx: ', i, 'num: ', num);

    const exp_num = target - num;

    const nums_copy = [...nums];
    nums_copy.splice(0, i + 1);

    if (nums_copy.indexOf(exp_num) > -1) {
      const target2_idx = nums_copy.indexOf(exp_num) + i + 1;

      return [i, target2_idx];
    }
  }
};

// const result = twoSum([2,7,11,15], 9);
// const result = twoSum([3,2,4], 6);
// const result = twoSum([3,3], 6);
const result = twoSum([0, 4, 3, 0], 0);
// const result = twoSum([-1,-2,-3,-4,-5], -8);

console.log('result: ', result);
