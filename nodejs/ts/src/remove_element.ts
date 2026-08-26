// 27. Remove Element (Easy)
// Удалить все вхождения val из массива nums in-place.
// Вернуть k — количество оставшихся элементов.
// Первые k элементов nums должны содержать значения != val.
// Порядок элементов может быть любым.

function removeElement(nums: number[], val: number): number {
    let j = 0; // указатель на позицию для записи следующего "хорошего" элемента

    for (let i = 0; i < nums.length; i++) {
        // если текущий элемент не равен val — записываем его на позицию j
        if (nums[i] !== val) {
            nums[j] = nums[i];
            j++; // сдвигаем указатель записи
        }
        // если равен val — просто пропускаем, j не двигается
    }

    return j; // j = количество элементов != val
}

// Тесты
function testRemoveElement(nums: number[], val: number, expected: number[]) {
    const k = removeElement(nums, val);
    const result = nums.slice(0, k).sort();
    const exp = [...expected].sort();
    console.assert(
        k === expected.length && JSON.stringify(result) === JSON.stringify(exp),
        `nums=${JSON.stringify(nums)}, val=${val}, got k=${k} ${JSON.stringify(result)}, expected k=${expected.length} ${JSON.stringify(exp)}`
    );
}

testRemoveElement([3,2,2,3], 3, [2,2]);
testRemoveElement([0,1,2,2,3,0,4,2], 2, [0,1,3,0,4]);
testRemoveElement([1], 1, []);
testRemoveElement([1], 2, [1]);
testRemoveElement([], 0, []);
testRemoveElement([4,4,4], 4, []);
testRemoveElement([1,2,3], 5, [1,2,3]);

console.log("All assertions passed!");
