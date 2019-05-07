#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int scale[5];
char tones[][5] = {"C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "B", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'"};
char tonalities[][6] = {"minor", "major"};
/*
char extension[][] = {"1", "b2", "2", "b3", "3", "4", "5", "b6", "6", "b7", "7", "8"};
*/

int translater(int * b, int length) {
    int * c = b + 4;
    for ( b ; b <= c ; b++){
        printf("%s\n", tones[*b]);
    };
    system("PAUSE");
    return 0;
};

int pentatonics(int a){
    int scale[5] = {a, a+2, a+4, a+7, a+9};
    translater(&scale[0], 5);
    return 0;
};

int main(){
    int a;
    printf("Type a number and you will get the tone with the according index: ");
    scanf("%d", &a);
    pentatonics(a);
    return 0;
};