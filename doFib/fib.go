package main

import (
	"fmt"
	"time"
)
	
func fib(n int) int {
	if n == 1 || n == 2{
		return 1
	} else {
		return fib(n - 1) + fib(n - 2)
	}
}

func main(){
	start := time.Now()
	result := fib(40)
	end := time.Now()
	time_diff := end.Sub(start)
	fmt.Println("斐波那契数列第40项的值为：",result,"用时:",time_diff)
}