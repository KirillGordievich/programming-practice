// func имя_функции (список_параметров) (типы_возвращаемых_значений){
// 		выполняемые_операторы
// }

package main

import "fmt"

func hello() {
	fmt.Println("Hello World")
}

func add(numbers ...int) {
	// В Go функция может принимать неопределенное количество параметров одного типа.
	// Например, нам надо получить сумму чисел, но мы точно не значем, сколько чисел будут переданы в функцию:
	var sum = 0
	for _, number := range numbers {
		sum += number
	}
	fmt.Println("sum = ", sum)
}

func add_return(x, y int) (z int) {
	z = x + y
	return
}

func add_return1(x, y int, firstName, lastName string) (z int, fullName string) {
	z = x + y
	fullName = firstName + " " + lastName
	return
}

func add_return2(x, y int) int {
	var z int = x + y
	return z
}

func some_func() (int, string) {
	var y int = 10
	var x string = "HELLO"
	return y, x
}

func main() {
	hello()
	add(5, 6, 7, 2, 3)
	var res int = add_return(1, 4)
	fmt.Println(res)

	res = add_return2(1, 4)

	fmt.Println(res)

	var res_int, res_string = some_func()
	fmt.Println(res_int)
	fmt.Println(res_string)

	anon_f := func(x, y int) int { return x + y }

	fmt.Println(anon_f(5, 1999))

}
