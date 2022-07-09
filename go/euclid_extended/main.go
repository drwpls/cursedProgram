package main

import (
	"fmt"
)

var qi, ri []int

var fast_input = false

func main() {

	var a, m, y, y0, q, y1, r int

	fmt.Println("Find a^-1 (mod m): ")
	if fast_input != false {
		fmt.Printf("a = ")
		fmt.Scan(&a)
		fmt.Printf("m = ")
		fmt.Scan(&m)
	} else {
		a = 550
		m = 1759
	}

	var a_s int = a
	var m_s int = m

	fmt.Printf("To solve the problem, find x satisfying the equation %d*x + %dy = 1\n", a, m)
	fmt.Printf("Go! \n\n")
	qi = []int{0, 0}
	ri = []int{m, a}

	y0 = 0
	y1 = 1
	for a > 0 {
		r = m % a
		if r == 0 {
			break
		}
		q = m / a

		qi = append(qi, q)
		ri = append(ri, r)

		fmt.Printf("%d = %d*%d + %d\n", m, a, q, r)
		y = y0 - y1*q
		y0 = y1
		y1 = y
		m = a
		a = r
	}
	if a > 1 {
		fmt.Println("a is not invertible in modulo m")
	} else {
		fmt.Println("\nResult: ")
		fmt.Println("1")
		var n int = len(qi)
		printRes(1, qi[n-1], n)
		fmt.Printf("Modulo inverse: %d^(-1) in modulo %d is %d\n", a_s, m_s, y)
	}

}

func printRes(a, b, i int) {

	fmt.Printf("= (%d) * (%d) - (%d) * (%d) \n", ri[i-3], a, ri[i-2], b)

	if i == 3 {
		return
	}

	fmt.Printf("= (%d) * (%d) - ((%d) - (%d) * (%d)) * (%d) \n\n", ri[i-3], a, ri[i-4], ri[i-3], qi[i-2], b)
	printRes(-b, -a-b*qi[i-2], i-1)
}
