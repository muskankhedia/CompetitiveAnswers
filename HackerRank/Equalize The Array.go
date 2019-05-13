package main

import (
    "fmt"
    "sort"
)

type count struct {
    a int
}

func main() {

    var n int
    var values []int

    fmt.Scanf("%d",&n)

    k := make([]int, n)
      for i := 0; i < n; i++ {
          fmt.Scan(&k[i])
    }

    sort.Ints(k)
    j := 0

    for i:= 1; i < n; i++ {

        if k[i] == k[i-1] {
        
            j++
        
        } else {

            values = append(values, j+1)
            j = 0
        
        }

        if i == n-1{
            values = append(values, j + 1)
        }
    }

    sort.Sort(sort.Reverse(sort.IntSlice(values)))
    max := values[0]
    left := n - max
    fmt.Println(left)

}


