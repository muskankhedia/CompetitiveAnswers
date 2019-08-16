package main

import (
	"fmt"
	"strings"
)

var res []string

func main() {

	var t int
	fmt.Scanf("%d", &t)

	i := 0
	for i < t {

		res = res[:0]

		var jack, dan string
		fmt.Scanln(&jack)
		fmt.Scanln(&dan)

		jack = jack + "0"
		dan = dan + "0"

		a := strings.Split(jack, "")
		b := strings.Split(dan, "")

		// fmt.Println("Jack: ", a)
		// fmt.Println("Daniel: ", b)

		l1 := len(a)
		l2 := len(b)
		le := l1 + l2

		for j := 0; j < le; j++ {

			// fmt.Println("j[0]: ", a[0])
			// fmt.Println("d[0]: ", b[0])
			if (strings.Compare(a[0], "0") == 0) {
				onlyAppend(b)
				break
			} else if (strings.Compare(b[0], "0") == 0) {
				onlyAppend(a)
				break
			} else {
				a1, b1 := check(a, b, 0)
				a = a1
				b = b1
			}

		}
		lenres := len(res)
		res = res[:lenres-1]
		fmt.Println(strings.Join(res, ""))
		// fmt.Println("i = ", i)
		i++
	}
	
}

func onlyAppend(a []string) {

	len := len(a)
	for i := 0; i < len; i++ {
		res = append(res, a[i])
	}

}

func check(a, b []string, j int) ([]string, []string) {

	l1 := len(a)
	l2 := len(b)
	// l = l1+l2
	if (strings.Compare(a[j], b[j]) == 1) {
		res = append(res, b[j])
		return a[:l1], b[1:l2]
	} else if (strings.Compare(a[j], b[j]) == -1) {
		res = append(res, a[j])
		return a[1:l1], b[:l2]
	} else {
		// j = j + 1
		// fmt.Println(check(a[j:l1], b[j:l2], j))
		res = append(res, a[j])
		return a[1:l1], b[:l2]
	}

	return a[:l1], b[:l2]
}
