#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char a[5];
char b[10];

int main(){
    scanf("%s", a);
    scanf("%s", b);
    printf("%d", strcmp(a, b));
    system("PAUSE");
};