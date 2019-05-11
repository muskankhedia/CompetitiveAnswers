package main

import (
	"fmt"
)

func main() {

	var n int
	fmt.Scanf("%d", &n)

	cycle := make([]int, n)
  	for i := 0; i < n; i++ {
		  fmt.Scan(&cycle[i])
	}

	sum := 1;

	for i := 0; i < n; i++ {
		for j := 1; j <= cycle[i]; j++{
			if (j%2 == 0){
				sum = sum + 1
			} else {
				sum = sum * 2
			}
		}
		fmt.Println(sum)

		sum = 1
	}
	
}

