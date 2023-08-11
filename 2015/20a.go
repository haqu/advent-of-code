package main

import (
    "os"
    "log"
)

func main() {
    log.Print("TOO SLOW")
    target:=33100000
    house:=770000
    max_presents:=0
    var (
        divisors []int
        presents int
        i int
    )
    for {
        house+=1
        divisors=[]int{1}
        for i=2;i<int(house/2)+1;i++ {
            if house%i==0 {
                divisors=append(divisors,i)
            }
        }
        if house>1 {
            divisors=append(divisors,house)
        }
        presents=0
        for _,d := range divisors {
            presents+=d*10
        }
        if presents>max_presents {
            max_presents=presents
            log.Printf("presents: %d, house: %d",presents,house)
            if presents>=target {
                log.Print("done")
                os.Exit(0)
            }
        }
    }
}

