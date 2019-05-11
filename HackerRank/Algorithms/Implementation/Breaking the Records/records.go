package main

import (
	"fmt"
)

func main() {

	var n int
	fmt.Scanf("%d", &n)

	k := make([]int, n)
  	for i := 0; i < n; i++ {
      	fmt.Scan(&k[i])
	}

	min := k[0]
	max := k[0]
	count_min := 0
    count_max := 0

	for i := 1;  i < n; i++ {
		if k[i] < min {
			min = k[i]
			count_min++
		} else if k[i] > max {
			max = k[i]
			count_max++
		}
	}

	fmt.Println(count_max, count_min)

}

