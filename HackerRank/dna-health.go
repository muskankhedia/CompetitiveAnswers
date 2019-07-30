package main

import(
	"fmt"
	"strings"
)

func main() {

	var n int

    fmt.Scanf("%d",&n)

    healthStr := make([]string, n)
    for i := 0; i < n; i++ {
	    fmt.Scan(&healthStr[i])
	}
	
	healthValue := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&healthValue[i])
	}

	var t int 
	fmt.Scanf("%d",&t)
	hv := make([]int, t+1)
	hv[0] = 0
	for (t > 0) {

		var start, end, c int
		var str string
		fmt.Scanf("%d", &start)
		fmt.Scanf("%d", &end)
		fmt.Scanln(&str)
		hv[t] = 0
		// fmt.Println("str: ", str)

		for i := start; i <= end; i++ {
			// fmt.Println("Reached")
			if (strings.Contains(str, healthStr[i])) {
				// fmt.Println("Reached1")
				c = 0
				lenSubstr := len(healthStr[i])
				for k := 0; k < len(str) - lenSubstr + 1; k++ {
					if str[k: k+lenSubstr] == healthStr[i] {
						c++
					}
				}
				// fmt.Println("count: ", c)
				hv[t] = hv[t] + healthValue[i] * c
				// fmt.Println(hv[t])
			}
		}
		// fmt.Println("%d", hv[t])
		t--
	}

	min, max := minMax(hv)
	fmt.Print(min," ", max)

}

func minMax(array []int) (int, int) {
    var max  = array[0]
    var min  = array[0]
    for _, value := range array {
        if max < value {
            max = value
        }
        if min > value {
            min = value
        }
    }
    return min, max
}
