package main
import (
    "fmt"
)
func main(){

    var m, n, r int
    fmt.Scanf("%d", &m)
    fmt.Scanf("%d", &n)
    fmt.Scanf("%d", &r)
    row := m
    col := n
    
    a := make([][]int, m)
      for i := 0; i < m; i++ {
        k := make([]int, n)
        for j := 0; j < n; j++ {
            fmt.Scan(&k[j])
        }
        a[i] = k
    }

    mini := min(m,n)
    if mini % 2 ==0 {
        k := mini / 2
        for r > 0 {
            for p := 0; p < k; p++ {
                i, j := p, p
                c := a[i][j]
                d := 0
                i++
                m = row - p
                n = col - p
                for i < m {
                    d = a[i][j]
                    a[i][j] = c
                    c = d
                    i++
                }
    
                i = m -1
                j = p + 1
                for j < n {
                    d = a[i][j]
                    a[i][j] = c
                    c = d
                    j++
                }
    
                i = m - 2
                j = n - 1
                for i >= p {
                    d = a[i][j]
                    a[i][j] = c
                    c = d
                    i--
                }
    
                i = p
                j = n - 2
                for j >= p {
                    d = a[i][j]
                    a[i][j] = c
                    c = d
                    j--
                }
            }
            r--

        }

        for i := 0; i < row; i++ {
            for j := 0; j < col; j++ {
                fmt.Printf("%d ",a[i][j])
                if(j==col-1){
                    fmt.Println("")
                }
            }
        }

    }



}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}