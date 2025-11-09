"use strict";
function countCharacters(str) {
    const count = {};
    for (const c of str) {
        count[c] = (count[c] || 0) + 1;
    }
    return count;
}
function sortCharactersByFrequency(str) {
    const charFrequency = countCharacters(str);
    const sortedChars = Object.keys(charFrequency).sort((a, b) => {
        return charFrequency[b] - charFrequency[a];
    });
    return sortedChars;
}
const str = "hello world";
console.log(countCharacters(str));
console.log(sortCharactersByFrequency(str));
