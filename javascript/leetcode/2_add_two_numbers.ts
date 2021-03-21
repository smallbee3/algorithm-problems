// from 13:29pm
// to 16:07pm

// Runtime: 400 ms, faster than 5.03%
// Memory Usage: 48.2 MB, less than 5.16%

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

const printListNode = (listNode) => {
  const output_arr = [];
  while (true) {
    output_arr.push(listNode.val);
    if (!listNode.next) break;
    listNode = listNode.next;
  }
  return output_arr;
};

const makeArrayFromListNode = (listNode) => {
  const resultArray = [];

  while (true) {
    resultArray.push(listNode.val);
    if (!listNode.next) {
      break;
    }
    listNode = listNode.next;
  }
  return resultArray;
};

const makeListNodeFromArray = (arr) => {
  let cur_listNode = null;
  let prev_listNode = undefined;
  arr.map((num) => {
    cur_listNode = new ListNode(num, prev_listNode);
    prev_listNode = cur_listNode;
  });
  return cur_listNode;
};

const sumOfTwoArray = (arr1, arr2) => {
  const arr_length = arr1.length > arr2.length ? arr1.length : arr2.length;

  console.log(1, { arr_length });

  const sum_arr = [];

  for (let i = 0; i < arr_length; i++) {
    const sum = (arr1[i] || 0) + (arr2[i] || 0);
    let digit = sum;

    if (sum > 9) {
      digit = sum - 10;
    }

    sum_arr[i] = sum_arr[i] ? sum_arr[i] + digit : digit;

    if (sum > 9) {
      sum_arr[i + 1] = 1;
    }
    // exceptional case with
    // const l1 = [9, 9, 9, 9, 9, 9, 9];
    // const l2 = [9, 9, 9, 9];
    if (sum_arr[i] > 9) {
      sum_arr[i + 1] = 1;
      sum_arr[i] = sum_arr[i] - 10;
    }

    console.log(2, { sum_arr });
  }
  console.log(3, { sum_arr });
  return sum_arr;
};

const reverseArr = (arr) => {
  const reversedArr = [];
  arr.map((n) => reversedArr.unshift(n));
  return reversedArr;
};

var addTwoNumbers = function (l1, l2) {
  let l1_num = 0;
  let l2_num = 0;
  const l1_arr = makeArrayFromListNode(l1);
  const l2_arr = makeArrayFromListNode(l2);
  //   l1_arr.map((num, idx) => (l1_num += num * 10 ** idx));
  //   l2_arr.map((num, idx) => (l2_num += num * 10 ** idx));
  console.log({ l1_arr });
  console.log({ l2_arr });

  const l3_num = sumOfTwoArray(l1_arr, l2_arr);
  console.log({ l3_num });

  const reversed_l3_num = reverseArr(l3_num);
  const result = makeListNodeFromArray(reversed_l3_num);
  return result;
};

// const l1 = [2, 4, 3];
// const l2 = [5, 6, 4];
// const l1 = [3, 4, 2];
// const l2 = [4, 6, 5];

// const l1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
// const l2 = [5,6,4]
// const l1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
// const l2 = [4,6,5]

// const l1 = [9, 9, 9, 9, 9, 9, 9];
// const l2 = [9, 9, 9, 9];

// const l1 = [0];
// const l2 = [0];

// const l1 = [9,9,9,9,9,9,9]
// const l2 = [9,9,9,9]

// const l1 = [2,4,9]
// const l2 = [5,6,4,9]
const l1 = [9, 4, 2];
const l2 = [9, 4, 6, 5];

const result = addTwoNumbers(
  makeListNodeFromArray(l1),
  makeListNodeFromArray(l2),
);

console.log(printListNode(result));
