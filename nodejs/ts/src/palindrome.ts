function isPalydrome(str: string): boolean {
    return str === str.split('').reverse().join('')
}

const notPalydrome = "Hello World";
const palydrome = "racecar";

console.log(isPalydrome(notPalydrome))
console.log(isPalydrome(palydrome))