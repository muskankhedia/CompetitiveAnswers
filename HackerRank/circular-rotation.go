package main

import (
	"fmt"
)

func main() {

	var n, k, q, t int
	fmt.Scanf("%d", &n)
	fmt.Scanf("%d", &k)
	fmt.Scanf("%d", &q)

	// sum := 0

	item := make([]int, n)
  	for i := 0; i < n; i++ {
		  fmt.Scan(&item[i])
	}
	

	item = rotateArray(item,n, k)

	for i := 0; i< q; i++ {
		fmt.Scanf("%d", &t)
		fmt.Println(item[t])
	}


}


func rotateArray(array []int, size, rotation int)[]int  {

	var newArray []int

	for i := 0; i < rotation; i++ {
		newArray = array[size-1:size]

		newArray = append(newArray, array[0:size-1]...)

		array = newArray
	}

	// fmt.Println(array)
	return array
}