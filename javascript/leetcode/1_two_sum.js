/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Approach 1: Brute Force
var twoSum = function(nums, target) {
    if (nums.length < 2) {
        return [];
    }
    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j]
            }
        }
    }
};

// Approach 2: Selective Search < Approach 2
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length - 1; i++) {
        
        counterPart = target - nums[i]
        console.log('counterPart: ', counterPart)
        index = nums.slice(i+1).indexOf(counterPart)
        console.log(i, index+i+1)
        if(index > -1) {
            return [i, index+i+1]
        }
    }
}

// result = twoSum([2, 7, 11, 15], 9)
result = twoSum([0, 4, 3, 0], 0)
console.log(result)
