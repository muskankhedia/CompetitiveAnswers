package main

import (
	"fmt"
	"sort"
)

func main() {

	var n, nk, nu int
	fmt.Scanf("%d", &n)
	fmt.Scanf("%d", &nk)
	fmt.Scanf("%d", &nu)

	k := make([]int, nk)
  	for i := 0; i < nk; i++ {
      	fmt.Scan(&k[i])
	}
	
	u := make([]int, nu)
  	for i := 0; i < nu; i++ {
      	fmt.Scan(&u[i])
	}

	sort.Ints(k)
	sort.Ints(u)
	most := -1

	for i := nk - 1; i >= 0; i-- {
		for j := nu - 1; j >= 0; j-- {
			if k[i] + u [j] <= n {
				if k[i] + u [j] > most {
					most = k[i] + u [j]
				}
				break;
			}
		}
	}

	fmt.Println(most)



}

