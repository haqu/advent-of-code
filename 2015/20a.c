// compile with optimization and run:
// clang -O3 -o 20a.exe 20a.c && ./20a

#include <stdio.h>
#include <stdlib.h>

typedef unsigned int u32;

int main() {
    u32 house=0;
    u32 target=33100000;
    u32 divisors[1024];
    int n_divisors=0;
    u32 i;
    u32 presents;
    u32 max_presents=0;
    double progress;
    while(1) {
        house+=1;
        n_divisors=0;
        divisors[n_divisors++]=1;
        for (i=2;i<house/2+1;i++) {
            if (house%i==0) {
                divisors[n_divisors++]=i;
            }
        }
        if (house>1) {
            divisors[n_divisors++]=house;
        }
        presents=0;
        for (i=0;i<n_divisors;i++) {
            presents+=divisors[i]*10;
        }
        if (presents>=max_presents) {
            max_presents=presents;
            if (presents>=target) {
                printf("presents: %d, house: %d\n",presents,house);
                exit(0);
            }
            progress=(1.0-(double)(target-max_presents)/target)*100;
            printf("presents: %d, house: %d, progress: %.0f%%\n",presents,house,progress);
        }
    }
    return 1;
}

