package main

import (
	"fmt"
)

func traversal(M [][]int, a, b, e, s int) {
	while (a != e && s < 2) {
		M[a][b] = M[a][b] + M[a+1][b]
		M[a+1][b] = M[a][b] - M[a+1][b]
		M[a][b] = M[a][b] - M[a+1][b]

		if (s == 0) {
			a = a + 1
		}
		else {
			a = a - 1
		}
	}

	while (b != e && s > 1) {
		M[a][b] = M[a][b] + M[a][b+1]
		M[a][b+1] = M[a][b] - M[a][b+1]
		M[a][b] = M[a][b] - M[a][b+1]

		if (s == 2) {
			b = b + 1
		}
		else {
			b = b - 1
		}
	}
	return M
}

func rotationMatrix(M [][]int, r, m, n int) {
	var c, hr, hc, tr, tc, temp int
	c = m / 2
	for i:=0; i< c; i++ {
		// initialising place pointers
		hr = i
		tr = m -1 -i
		hc = i
		tc = n -1 -i

		M = traversal(M, hr, hc, tr, 0)
		M = traversal(M, tr, hc, tc, 1)

		hr, hc = i, i

		M = traversal(M, tr, tc, hr, 2)
		M = traversal(M, hr, tc, hc, 3)
		temp = M[hc][hc+1]
		M[hc][hc+1] = M[hc][hc]
		M[hc][hc] = temp

		// printing matrix


	}

}

func main() {
	var m, n, r int
	fmt.Scanf("%d %d %d", &m, &n, &r)
	var M [m][n]int
	for i:=0; i< m; i++ {
		for j:=0; j<n; j++ {
			fmt.Scanf("%d", &M[i][j])
		}
	}
	rotationMatrix(M, r, m, n)
}

