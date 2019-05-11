package main

import (
    "fmt"
    "math"
)

func main() {

    var n,k int
    fmt.Scanf("%d", &n)
    fmt.Scanf("%d", &k)

    arr := make([]int, n)
      for i := 0; i < n; i++ {
          fmt.Scan(&arr[i])
    }

    count := make([]int, k)
    final := 0.0
    for i := 0; i < n; i++ {
        count[arr[i]%k]++
    }

    if k%2 == 0 {

        for i:= 1; i < int(k/2) ; i++ {

            final = final + math.Max(float64(count[i]), float64(count[k - i]))

        }

        if count[k/2] >= 1 {
            final++
        }


    } else {

        for i:= 1; i < int(k/2) + 1; i++ {

            final = final + math.Max(float64(count[i]), float64(count[k - i]))

        }
    
    }

    if count[0] >= 1 {
        final++
    }

    fmt.Println(int(final))
}
