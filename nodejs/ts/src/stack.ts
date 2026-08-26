// Реализовать стек, который поддерживает метод удаления, добавления элементов и метод, который возвращает максимальный по значению элемент в стеке за О(1)


class MaxStack<T> {

    private readonly stack: T[];
    private readonly max_elements: T[];

    constructor() {
        this.stack = []
        this.max_elements = []
    }

    push(value: T): void {
        this.stack.push(value);

        if (this.max_elements.length === 0 || value >= this.max_elements[this.max_elements.length - 1]) {
            this.max_elements.push(value);
        }
    }

    pop(): T | undefined {
        const popped = this.stack.pop();

        if (popped === this.max_elements[this.max_elements.length - 1]) {
            this.max_elements.pop();
        }

        return popped;
    }

    max(): T {
        if (this.stack.length === 0) {
            throw new Error('Empty stack');
        }

        return this.max_elements[this.max_elements.length - 1];
    }
}

// --- Tests ---

const s1 = new MaxStack<number>();
s1.push(5);
console.assert(s1.max() === 5, 'один элемент: max = 5');

s1.push(3);
console.assert(s1.max() === 5, 'push меньшего: max остаётся 5');

s1.push(7);
console.assert(s1.max() === 7, 'push большего: max = 7');

console.assert(s1.pop() === 7, 'pop возвращает 7');
console.assert(s1.max() === 5, 'после pop max = 5');

s1.pop();
s1.pop();
console.assert(s1.pop() === undefined, 'pop из пустого = undefined');

const s2 = new MaxStack<number>();
s2.push(5);
s2.push(5);
console.assert(s2.max() === 5, 'дубликаты: max = 5');
s2.pop();
console.assert(s2.max() === 5, 'после pop дубликата: max = 5');

const s3 = new MaxStack<number>();
s3.push(2);
s3.push(1);
s3.push(4);
s3.push(3);
console.assert(s3.max() === 4, 'смешанный: max = 4');
s3.pop();
console.assert(s3.max() === 4, 'pop 3: max = 4');
s3.pop();
console.assert(s3.max() === 2, 'pop 4: max = 2');

const s4 = new MaxStack<number>();
s4.push(-3);
s4.push(-1);
s4.push(-2);
console.assert(s4.max() === -1, 'отрицательные: max = -1');

const s5 = new MaxStack<number>();
try { s5.max(); console.assert(false, 'должен бросить ошибку'); } catch {}

console.log('All tests passed');
