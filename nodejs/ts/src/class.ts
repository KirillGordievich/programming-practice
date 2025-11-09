class User {
    readonly name: string
    readonly age: number

    constructor (userName: string, userAge: number) {
        this.name = userName;
        this.age = userAge;
    }
}

const kirill = new User("Kirill", 25)

console.log(kirill)