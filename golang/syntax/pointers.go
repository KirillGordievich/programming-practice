package main

import "fmt"

func main() {

	var x int = 4   // определяем переменную
	var p *int = &x // определяем указатель
	fmt.Println(x)
	fmt.Println(p)  // значение самого указателя - адрес переменной x
	fmt.Println(*p) // значение самого указателя - адрес переменной x

	*p = 10
	fmt.Println(x)

	var pf *float64
	if pf != nil {
		fmt.Println("Value:", *pf)
	}

}
