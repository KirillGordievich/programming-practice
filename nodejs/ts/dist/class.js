"use strict";
class User {
    constructor(userName, userAge) {
        this.name = userName;
        this.age = userAge;
    }
}
const kirill = new User("Kirill", 25);
console.log(kirill);
kirill.age = 26;
