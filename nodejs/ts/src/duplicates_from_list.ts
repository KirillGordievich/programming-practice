
class ListNode {
    val: number
    next: ListNode | null

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

// вспомогательные функции для тестов
function fromArray(arr: number[]): ListNode | null {
    if (!arr.length) return null;
    const head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

function toArray(head: ListNode | null): number[] {
    const result: number[] = [];
    while (head) {
        result.push(head.val);
        head = head.next;
    }
    return result;
}

function deleteDuplicates(head: ListNode | null): ListNode | null {
    let current: ListNode | null = head;

    while (current && current.next !== null) {
        if (current.val === current.next.val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }

    return head;
}

// Тесты
// Input: [1,1,2] -> Output: [1,2]
console.assert(JSON.stringify(toArray(deleteDuplicates(fromArray([1,1,2])))) === JSON.stringify([1,2]), "[1,1,2] -> [1,2]");

// Input: [1,1,2,3,3] -> Output: [1,2,3]
console.assert(JSON.stringify(toArray(deleteDuplicates(fromArray([1,1,2,3,3])))) === JSON.stringify([1,2,3]), "[1,1,2,3,3] -> [1,2,3]");

// Input: [1,1,1] -> Output: [1]
console.assert(JSON.stringify(toArray(deleteDuplicates(fromArray([1,1,1])))) === JSON.stringify([1]), "[1,1,1] -> [1]");

// Input: [1,2,3] -> Output: [1,2,3] (нет дубликатов)
console.assert(JSON.stringify(toArray(deleteDuplicates(fromArray([1,2,3])))) === JSON.stringify([1,2,3]), "[1,2,3] -> [1,2,3]");

// Input: [] -> Output: []
console.assert(JSON.stringify(toArray(deleteDuplicates(fromArray([])))) === JSON.stringify([]), "[] -> []");

// Input: [1] -> Output: [1]
console.assert(JSON.stringify(toArray(deleteDuplicates(fromArray([1])))) === JSON.stringify([1]), "[1] -> [1]");

console.log("All assertions passed!");
