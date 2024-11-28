package main

import "fmt"

func main() {
	var people = map[string]int{
		"Tom":   1,
		"Bob":   2,
		"Sam":   4,
		"Alice": 8,
	}
	fmt.Println(people) // map[Tom:1 Bob:2 Sam:4 Alice:8]
	fmt.Println(len(people))

	delete(people, "Bob")

	fmt.Println(people) // map[Tom:1 Bob:2 Sam:4 Alice:8]
	fmt.Println(len(people))

}
