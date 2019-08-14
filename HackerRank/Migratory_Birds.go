package main

import (
    "fmt"
)

func main() {

    var n int
    var values []int

    fmt.Scanf("%d",&n)

    k := make([]int, n)
    for i := 0; i < n; i++ {
	    fmt.Scan(&k[i])
    }

	for i := 0; i < n; i++ {
		values[k[i]-1]++
	}

	var m, max int

	if len(values) > 0 {
        m = values[0]
    }
    for i := 1; i < len(values); i++ {
        if values[i] > m {
			m = values[i]
			max = i+1
        }
	}
	fmt.Print(max)

}