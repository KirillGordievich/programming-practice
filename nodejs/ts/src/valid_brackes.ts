// Маппинг открывающих скобок к закрывающим
const BRACKET_MAP: Record<string, string> = {
    '{': '}',
    '(': ')',
    '[': ']'
};

function isValid(s: string): boolean {
    const stack: string[] = []; // стек для хранения открывающих скобок

    for (const char of s) {
        // если символ — открывающая скобка, кладём в стек
        if (char in BRACKET_MAP) {
            stack.push(char);
            continue;
        }

        // берём последнюю открывающую скобку из стека
        const last_char = stack[stack.length - 1];

        // если её закрывающая пара не совпадает с текущим символом — невалидно
        if (BRACKET_MAP[last_char] !== char) {
            return false;
        }

        // пара совпала — убираем открывающую из стека
        stack.pop();
    }

    // если стек пуст — все скобки закрыты корректно
    return stack.length === 0;
}

// Тесты
console.assert(isValid("()") === true, "simple pair");
console.assert(isValid("()[]{}") === true, "multiple pairs");
console.assert(isValid("{[]}") === true, "nested valid");
console.assert(isValid("([)]") === false, "interleaved invalid");
console.assert(isValid("(") === false, "unclosed bracket");
console.assert(isValid(")") === false, "no opening bracket");
console.assert(isValid("") === true, "empty string is valid");
console.assert(isValid("((()))") === true, "deep nesting");
console.assert(isValid("({[)]}") === false, "mixed interleaved");

console.log("All assertions passed!");
