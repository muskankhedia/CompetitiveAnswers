package main

import (
	"fmt"
)

type block struct {
	value int
	ladd *block
	radd *block
}

func inorder(a block) {
	fmt.Println(a.value)
	if a.ladd != nil {
		inorder(*a.ladd)
	}
	if a.radd != nil {
		inorder(*a.radd)
	}
}

// the below function is for pure BST implementation
func main() {
	var (
		n int
		BST []block
	)
	fmt.Scanf("%d", &n)
	for i:=0; i< n; i++ {
		var t block
		fmt.Scanf("%d", &t.value)
		t.ladd=nil
		t.radd=nil
		BST = append(BST, t)
	}
	// forming tree
	for i:=0; i< n; i++ {
		for j:=0; j<i;j++ {
			if BST[j].value > BST[i].value {
				if BST[j].ladd == nil {
					BST[j].ladd = &BST[i]
				}
			} else {
				if BST[j].radd == nil {
					BST[j].radd = &BST[i]
				}
			}
		}
	}
	// var q int
	// fmt.Scanf("%d", &q)
	// for i:=0;i<n; i++ {
	// 	if q == BST[i].value {
	// 		inorder(BST[i])
	// 		break
	// 	}
	// }
}