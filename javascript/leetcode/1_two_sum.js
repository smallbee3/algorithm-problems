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

// Approach 2: Selective Search > Approach 1
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

// twoSum([2, 7, 11, 15], 9)
// twoSum([0, 4, 3, 0], 0)



// 200331
// Approach 3: Selective Search (timeover)
// ( JS array method < for loop with index)

var twoSum = function(nums, target) {
    let result = [];
    nums.some((element, index, arr) => {
        if (target - element === element) {
            arr.forEach((element2, index) => {
                if (element === element2) result.push(index);
            });
            
            if (result.length > 1) {
                return true;
            }
            result = [];
        }

        else if (arr.indexOf(target - element) > -1) {
            result = [index, arr.indexOf(target - element)];
            return true;
        }
    });
    return result;
};



// twoSum([2, 7, 11, 15], 9);
// twoSum([3, 3], 6);
twoSum([3, 2, 4], 6);
