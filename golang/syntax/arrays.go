package main

import "fmt"

func main() {
	var numbers [5]int = [5]int{1, 2, 3, 4}
	fmt.Println(numbers)

	fmt.Println(numbers[0]) // 1
	fmt.Println(numbers[4]) // 0

	numbers[0] = 87
	fmt.Println(numbers) // 87

	// Если в квадратных скобках вместо длины указано троеточие, то длина массива определяется, исходя из количества переданных ему элементов:
	var numbers2 = [...]int{1, 2, 3, 4, 5} // длина массива 5
	fmt.Println(numbers2)                  // [1 2 3]

	// Также можно применять сокращенное определение переменной массива:
	numbers3 := [...]int{4, 4, 1, 2, 0} // длина массива 5
	fmt.Println(numbers3)               // [1 2 3]

	for i, v := range numbers3 {
		fmt.Println(i, v)
	}

	fmt.Println(len(numbers))
}
