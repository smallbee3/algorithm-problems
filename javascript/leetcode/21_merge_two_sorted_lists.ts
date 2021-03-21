/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

// from 19:51pm
// from 21:14pm

// Runtime: 240 ms, faster than 5.15%
// Memory Usage: 48.2 MB, less than 5.28%

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

const printListNode = (node) => {
  if (!node) return [];

  const output_arr = [];

  while (true) {
    output_arr.push(node.val);
    if (!node.next) break;
    node = node.next;
  }
  return output_arr;
};

const makeArrayFromListNode = (node) => {
  if (!node) return [];
  const resultArray = [];

  while (true) {
    resultArray.push(node.val);
    if (!node.next) {
      break;
    }
    node = node.next;
  }
  return resultArray;
};

const makeListNodeFromArray = (arr) => {
  let cur_node = null;
  let prev_node = undefined;
  arr.map((num) => {
    cur_node = new ListNode(num, prev_node);
    prev_node = cur_node;
  });
  return cur_node;
};

const reverseArr = (arr) => {
  const reversedArr = [];
  arr.map((n) => reversedArr.unshift(n));
  return reversedArr;
};

const insertSort = (l1_arr, l2_arr) => {
  if (l1_arr.length === 0) return l2_arr;
  if (l2_arr.length === 0) return l1_arr;

  l1_arr.map((num1, idx1) => {
    for (let idx2 = 0; idx2 < l2_arr.length; idx2++) {
      const num2 = l2_arr[idx2];

      if (num1 <= num2) {
        l2_arr.splice(idx2, 0, num1);
        break;
      }

      if (idx2 === l2_arr.length - 1) {
        l2_arr.splice(idx2 + 1, 0, num1);
        break;
      }
    }
  });

  return l2_arr;
};

var mergeTwoLists = function (l1, l2) {
  const l1_arr = makeArrayFromListNode(l1);
  const l2_arr = makeArrayFromListNode(l2);

  console.log({ l1_arr });
  console.log({ l2_arr });

  const merged_arr = insertSort(l1_arr, l2_arr);

  const merged_arr_reversed = reverseArr(merged_arr);
  console.log({ merged_arr_reversed });
  return makeListNodeFromArray(merged_arr_reversed);
};

// const l1 = [1, 2, 4];
// const l2 = [1, 3, 4];
// const l1 = [4, 2, 1];
// const l2 = [4, 3, 1];
// const l1 = []
// const l2 = [0]
// const l1 = [];
// const l2 = [];
// const l1 = [1];
// const l2 = [];
const l1 = [2];
const l2 = [1];

const result = mergeTwoLists(
  makeListNodeFromArray(l1),
  makeListNodeFromArray(l2),
);

console.log(printListNode(result));
