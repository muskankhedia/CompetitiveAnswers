package main

import "fmt"

type input struct {
	cat_a int
	cat_b int
	mouse_c int
}


func main() {

	var n int
	var in input
	var store []input

	fmt.Scanf("%d",&n)

	i := 0
	for ; i < n; {
		fmt.Scanf("%d",&in.cat_a)
		fmt.Scanf("%d",&in.cat_b)
		fmt.Scanf("%d",&in.mouse_c)
		store = append(store, in)
		i++
	}
    
	diff1 := 0
	diff2 := 0
	
	for _, res := range store {
		if res.cat_a <= res.mouse_c && res.cat_b <= res.mouse_c {
			diff1 = res.mouse_c - res.cat_a
			diff2 = res.mouse_c - res.cat_b
		} else if res.cat_a >= res.mouse_c && res.cat_b >= res.mouse_c{

			diff1 = res.cat_a - res.mouse_c 
			diff2 = res.cat_b - res.mouse_c 

		} else if res.cat_a <= res.mouse_c {

			diff1 = res.mouse_c - res.cat_a
			diff2 = res.cat_b - res.mouse_c 
			
		} else if res.cat_b <= res.mouse_c {

			diff1 = res.cat_a - res.mouse_c 
			diff2 = res.mouse_c - res.cat_b
		} else {
			diff1 = 0
            diff2 = 0
		}

		if diff1 < diff2 {
			fmt.Println("Cat A")
		} else if diff1 > diff2 {
			fmt.Println("Cat B")
		} else {
			fmt.Println("Mouse C")
		}
	}

}

