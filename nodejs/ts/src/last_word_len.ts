// Given a string s consisting of words and spaces, return the length of the last word in the string.
// A word is a maximal substring consisting of non-space characters only.

function lengthOfLastWord(s: string): number {
    // убираем пробелы по краям, разбиваем по пробелу, берём последний элемент
    return s.trim().split(' ').pop()!.length;
}

// Тесты
console.assert(lengthOfLastWord("Hello World") === 5, "simple two words");
console.assert(lengthOfLastWord("   fly me   to   the moon  ") === 4, "trailing spaces");
console.assert(lengthOfLastWord("luffy is still joyboy") === 6, "no trailing spaces");
console.assert(lengthOfLastWord("a") === 1, "single char");
console.assert(lengthOfLastWord("   a   ") === 1, "single char with spaces");

console.log("All assertions passed!");
