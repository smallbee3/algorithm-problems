/**
 * Definition for singly-linked list.
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function ListNode(val) {
    this.val = val;
    this.next = null;
}


// 1) (fail)

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



// 200331
// 2) (fail)
// result = addTwoNumbers(makeLinkedList(1000000000000000000000000000001), makeLinkedList(465))

function ListNode(val) {
    this.val = val;
    this.next = null;
}

function printLinkedList(l) {
    let numStr = ''
    while(true) {
        numStr += l.val
        if (!l.next) break;
        numStr += ' -> '
        l = l.next
    }
    console.log(numStr)
}

function makeLinkedList(num) {
    numList = [];
    idx = 1;
    while(true) {
        numList.unshift(num % 10);
        num = Math.floor(num / 10);
        if (num < 1) break;
        idx++;
    }
    console.log(2, numList)

    // const numStr = String(num);
    let prev;
    for(let i=0; i < numList.length; i++) {
        l = new ListNode(numList[i])
        if (prev) l.next = prev
        prev = l
    }
    return l
}

function makeNum(l) {
    let num = 0;
    let idx = 1;
    while(true) {
        num += l.val * 10 ** (idx - 1);
        if (!l.next) break;
        l = l.next;
        idx++;
    }
    return num;
}

var addTwoNumbers = function(l1, l2) {
    num3 = makeNum(l1) + makeNum(l2)
    console.log(num3)
    l3 = makeLinkedList(num3)
    return l3
};

printLinkedList(makeLinkedList(342))
printLinkedList(makeLinkedList(465))
result = addTwoNumbers(makeLinkedList(342), makeLinkedList(465))
printLinkedList(result)

// printLinkedList(makeLinkedList(10000000000000000001))
// printLinkedList(makeLinkedList(465))
// result = addTwoNumbers(makeLinkedList(1000000000000000000000000000001), makeLinkedList(465))
// printLinkedList(result)




// 200401
// 3) (retrial)

function ListNode(val) {
    this.val = val;
    this.next = null;
}

function printLinkedList(l) {
    let numStr = ''
    while(true) {
        numStr += l.val
        if (!l.next) break;
        numStr += ' -> '
        l = l.next
    }
    console.log('(', numStr, ')')
}

function makeLinkedList(value) {
    let prevNode = null;
    let node = null;
    for (var i of value.toString()) {
        node = new ListNode(Number(i))
        if (prevNode) {
            node.next = prevNode;
        }
        prevNode = node;
    }
    return node;
}

// ----------------------------------------------------

function makeLinkedListFromArr(arr) {
    let prev;
    for(let i=arr.length-1; i >= 0; i--) {
        node = new ListNode(arr[i]);
        if (prev) node.next = prev;
        prev = node;
    }
    return node;
}

function arraySum(arr1, arr2) {
    let sumArr = [];
    [arrMain, arrSub] = arr1.length > arr2.length ? [arr1, arr2] : [arr2, arr1]

    for (let i = 0; i < arrMain.length; i++) {
        // arrMain + arrSub
        if (i < arrSub.length) {
            sumArr.push(arrMain[i] + arrSub[i]);
        }
        // arrMain
        else {
            sumArr.push(arrMain[i]);
        }
    }
    console.log('before : ', sumArr);

    for (let i = 0; i < sumArr.length; i++) {
        if (sumArr[i] > 9) {
            quotient = Math.floor(sumArr[i] / 10);
            remainder = sumArr[i] % 10;

            sumArr[i] = remainder;
            // [10] -> [0, 1]
            if (typeof(sumArr[i+1]) === 'number') {
                sumArr[i+1] += quotient;
            }
            else {
                sumArr.push(quotient);
            }
        }
    }
    console.log('after  : ', sumArr);

    return sumArr
}

function makeNumArr(l) {
    let numArr = [];
    while(true) {
        numArr.push(l.val);
        if (!l.next) break;
        l = l.next;
    }
    return numArr;
}

var addTwoNumbers = function(l1, l2) {
    sumArr = arraySum(makeNumArr(l1), makeNumArr(l2));
    l = makeLinkedListFromArr(sumArr);
    return l;
};

printLinkedList(makeLinkedList(342));
printLinkedList(makeLinkedList(465));
result = addTwoNumbers(makeLinkedList(342), makeLinkedList(465));
printLinkedList(result);



// printLinkedList(makeLinkedList(10000000000000000001))
// printLinkedList(makeLinkedList(465))
// result = addTwoNumbers(makeLinkedList(1000000000000000000000000000001), makeLinkedList(465))
// printLinkedList(result)
