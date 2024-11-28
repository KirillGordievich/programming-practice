package main

import "fmt"

type person struct {
	name string
	age  int
}

func (p *person) updateAge(newAge int) {
	(*p).age = newAge
}

func (p person) updateAgeNoPointer(newAge int) {
	p.age = newAge
}

func main() {
	var tom = person{name: "Tom", age: 24}
	var tomPointer *person = &tom
	fmt.Println("before update", tom.age)
	tomPointer.updateAge(33)
	fmt.Println("after update", tom.age)

	fmt.Println("before no pointer update", tom.age)
	tomPointer.updateAgeNoPointer(25)
	fmt.Println("after no pointer update", tom.age)
}
