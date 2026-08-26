/*
Есть массив, каждый элемент которого может быть либо типа string, либо типа array, 
типы значения которого также могут быть как у корневого массива. 

Пример: ['a', 'b',[ 'c', 'd'],[ 'e', 'f',['g'],'h'],'i'] 

Требуется вывести в консоль данный массив в виде иерархии: 
-a
-b
--c
--d
--e
--f
---g
--h
-i

Решение должно быть универсальным.

*/

type NestedArray = (string | NestedArray)[];

const PREFIX = '-';

function formatArray(arr: NestedArray, prefix = PREFIX): string {
  let result = '';
  for (const item of arr) {
    if (Array.isArray(item)) {
      result += formatArray(item, prefix + PREFIX);
    } else {
      result += prefix + item + '\n';
    }
  }
  return result;
}

const arr = ['a', 'b', ['c', 'd', 'e', 'f', ['g'], 'h', ['j']], 'i'];
console.log(formatArray(arr));

console.log('-------\n');

const arr2 = ['a', 'b', ['c', 'd'], ['e', 'f', ['g'], 'h'], 'i'];
console.log(formatArray(arr2));
