package main

import "fmt"

type person struct {
	name string
	age  int
}

func main() {

	var tom person = person{name: "Tom", age: 24}
	fmt.Println(tom.name, tom.age) // 24

	tom.age = 38                   // изменяем значение
	fmt.Println(tom.name, tom.age) // Tom 38

	var tomPointer *person = &tom
	tomPointer.age = 29
	fmt.Println(tom.name, tom.age)
}
