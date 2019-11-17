/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function makeNum(llist) {
    let num = 0;
    while (true) {
        let i = 0
        if (llist) {
            num += llist.val * (10 ** i);
            llist = llist.next;
            ++i;
        }
        else {
            break;
        }
    }
    return num;
}
function makeLlist(value) {
    let prevNode = null;
    let node = null;
    for (var i of value.toString()) {
        node = new ListNode(i)
        if (prevNode) {
            node.next = prevNode;
        }
    }
    return node;
}
var addTwoNumbers = function(l1, l2) {
    console.log(1, makeNum(l1))
    console.log(2, makeNum(l2))
    const sumNum = makeNum(l1) + makeNum(l2)
    console.log(3, sumNum)
    return makeLlist(sumNum)
};