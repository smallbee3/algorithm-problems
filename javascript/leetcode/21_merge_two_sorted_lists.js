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

function ListNode(val) {
    this.val = val;
    this.next = null;
}

var mergeTwoLists = function(l1, l2) {
    
    function makeArrayFromList(l) {
        let array = [];

        // [], [] -> null, null
        // if (!l) return array;

        // while (true) {
        //     array.push(l.val);
        //     if (l.next !== null) {
        //         l = l.next;
        //     }
        //     else {
        //         break;
        //     }
        // }

        while (l) {
            array.push(l.val)
            l = l.next
        }

        return array;
    }

    function makeListFromArray(arr) {
        let node = null;
        let prevNode = null;
        for (let i of arr) {
            node = new ListNode(i);
            node.next = prevNode;
            prevNode = node;
        }
        return node;
    }

    function quickSortReverse(arr) {
        if (arr.length < 2) return arr

        const index = Math.floor(arr.length/2)
        const pivot = arr[index]
        arr.splice(index, 1)
        const lessThan = arr.filter(num => num <= pivot)
        const moreThan = arr.filter(num => num > pivot)
        return [...quickSortReverse(moreThan), pivot, ...quickSortReverse(lessThan)]
    }

    summedArray = makeArrayFromList(l1).concat(makeArrayFromList(l2));
    console.log({summedArray});
    // sortedArray = summedArray.sort().reverse();
    sortedArray = quickSortReverse(summedArray);
    console.log({sortedArray});

    return makeListFromArray(sortedArray);
};


// [ QuickSort in javascript ]
function quickSort(arr) {
    if (arr.length < 2) return arr

    const index = Math.floor(arr.length/2)
    const pivot = arr[index]
    arr.splice(index, 1)
    const lessThan = arr.filter(num => num <= pivot)
    const moreThan = arr.filter(num => num > pivot)
    return [...quickSort(lessThan), pivot, ...quickSort(moreThan)]
}

// result = quickSort([-10, -6, -6, -6, -3, 5 ]);
// console.log(result)
