package main

import (
	"fmt"
)

func main() {

	var t = 0
	var x = 1988
	var n = 11
	for x > 0 {
		t = 0
		for n > 0 {
			t = t + ((n%10) * (n%10))
			n = n/10
		}
		n = t
		fmt.Println(n)
		x--;
	}
	fmt.Println(n)


}