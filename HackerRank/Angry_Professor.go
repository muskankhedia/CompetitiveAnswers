package main

func main() {

	var t, students, threshold, count int
    var values []int

    fmt.Scanf("%d",&t)

	for i:= 0; i < t; i++ {

		fmt.Scanf("%d",&students)
		fmt.Scanf("%d",&threshold)

		time := make([]int, students)
		for i := 0; i < students; i++ {
			fmt.Scan(&time[i])
			if time[i] <= 0 {
				count++
			}
		}
		if count >= threshold {
			fmt.Print("NO")
		} else {
			fmt.Print("YES")
		}
	
	}
    
}