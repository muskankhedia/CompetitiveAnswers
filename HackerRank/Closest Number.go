package main

import (
	"fmt"
	"math"
)
type input struct {
	a float64
	b float64
	x int
}

func main() {

	var n int
	var in input
	var store []input

	fmt.Scanf("%d",&n)

	i := 0
	for ; i < n; {
		fmt.Scanf("%f",&in.a)
		fmt.Scanf("%f",&in.b)
		fmt.Scanf("%d",&in.x)
		store = append(store, in)
		i++;
	}	

	for _, res := range store {
		exp := math.Pow(res.a, res.b)
		d := int(exp) + res.x / 2;
		fmt.Println(d - (d % res.x))
	}
}

