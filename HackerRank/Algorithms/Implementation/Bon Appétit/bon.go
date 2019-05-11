package main

import (
	"fmt"
)

func main() {

	var n, k, charged int
	fmt.Scanf("%d", &n)
	fmt.Scanf("%d", &k)

	sum := 0

	item := make([]int, n)
  	for i := 0; i < n; i++ {
		  fmt.Scan(&item[i])
		  sum += item[i]
	}
	
	fmt.Scanf("%d", &charged)

	acc := sum - item[k] 

	 if acc / 2 == charged {
		fmt.Println("Bon Appetit");
	} else {
		fmt.Println(charged - acc / 2);
	}


}

