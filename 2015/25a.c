// compile with optimization and run:
// clang -O3 -o 25a.exe 25a.c && ./25a

#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long u64;

int main() {
    int row=2947;
    int col=3029;
    //row=2,col=1; //DEBUG
    int index=1;
    for (int r=2;r<=row;r++) {
        index+=r-1;
    }
    for (int c=2;c<=col;c++) {
        index+=(row+c-1);
    }
    printf("index: %d\n",index);
    u64 v=20151125;
    for (int i=2;i<=index;i++) {
        v=(v*252533)%33554393;
    }
    printf("value: %llu\n",v);
    return 1;
}

