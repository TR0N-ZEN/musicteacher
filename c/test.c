#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int a = 12;


int level1(){
    printf("level1");
};

int main(){
    printf("%d", &a);
    system("PAUSE");
};