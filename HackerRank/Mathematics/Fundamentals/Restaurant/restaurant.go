package main

import "fmt"

type details struct {
	mid int
	used int
	unused int
}

type input struct {
	len int
	br int
}



func main() {

	var n, midL, midB, least, ft int
	// var final []int
	var in input
	var store []input
	var dt details
	var d []details

	ft = 0
	least = 10000
	fmt.Scanf("%d",&n)

	for i := 0; i < n; i++  {
		fmt.Scanf("%d",&in.len)
		fmt.Scanf("%d",&in.br)
		store = append(store, in)
	}	

	for _,res := range store {
		
		if res.len <= res.br {

			for j := 1 ; j <= res.len; j++ {

				for k := 1; k <= res.len + 1; k++ {
					if j*k > res.len {
						midL = k - 1;
						// fmt.Println("midL: ", midL)
						break;
					}
				}
				for l := 1; l <= res.br + 1; l++ {
					if j*l > res.br {
						midB = l - 1;
						// fmt.Println("midB: ", midB)
						break;
					}
				}
				// fmt.Println("j", j)
				dt.mid = midL * midB
				// fmt.Print(dt.mid, " ")
				dt.used = dt.mid * (j) * j
				dt.unused = (res.len * res.br) - dt.used
				if dt.unused <= least {
					least = dt.unused;
					ft = dt.mid
				}
				// fmt.Println(dt.used)
				d = append(d, dt)
			}
			fmt.Println(ft)
		} else {
			for j := 1 ; j <= res.br; j++ {

				for k := 1; k <= res.len + 1; k++ {
					if j*k > res.len {
						midL = k - 1;
						// fmt.Println("midL: ", midL)
						break;
					}
				}
				for l := 1; l <= res.br + 1; l++ {
					if j*l > res.br {
						midB = l - 1;
						// fmt.Println("midB: ", midB)
						break;
					}
				}
				// fmt.Println("j", j)
				dt.mid = midL * midB
				// fmt.Print(dt.mid, " ")
				dt.used = dt.mid * (j) * j
				dt.unused = (res.len * res.br) - dt.used
				if dt.unused <= least {
					least = dt.unused;
					ft = dt.mid
				}
				// fmt.Println(dt.used)
				d = append(d, dt)
			}
			fmt.Println(ft)
		}
	}
}

