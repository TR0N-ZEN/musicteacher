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
    int * c = b + length;
    for ( b ; b <= c ; b++){
        printf("%s\n", tones[*b]);
    };
    system("PAUSE");
    return 0;
};

int major_pentatonics(int a){
    int scale[5] = {a, a+2, a+4, a+7, a+9};
    translater(&scale[0], 4);
    return 0;
};

int minor_pentatonics(int a){
    int scale[5] = {a, a+3, a+5, a+7, a+10};
    translater(&scale[0], 4);
    return 0;
};

int major_heptatonics(int a){
    int scale[7] = {a, a+2, a+4, a+5, a+7, a+9, a+11};
    translater(&scale[0], 6);
    return 0;
};

int minor_heptatonics(int a){
    int scale[7] = {a, a+2, a+3, a+5, a+7, a+8, a+11};
    translater(&scale[0], 6);
    return 0;
};

int main(){
    char a[5];
    int b;
    printf("Type a root: ");
    scanf("%s", a);
    for(int x = 0; x < 37; x++){
        if(strcmp(a, tones[x]) == 0){
            b = x;
            break;
        };
    };
    while(1)   // execute 'forever'
      {
       int choice=-1;
       while(choice <=0 || choice > 5)    // ignore any invalide choice
          {
           printf("\nSelect a \n"
                   "  1: major pentatonics\n  2: minor pentatonics\n  3: major heptatonics\n"
                   "  4: minor heptatonics\n  5:  Exit\n");
           scanf("%d", &choice);
           }
       // valid choice enter, execute command
       switch (choice)
           {
           case 1: // statements to open file
                   printf("\nmajor pentatonics\n");
                   major_pentatonics(b);
                   break;
           case 2: // statements to process data
                   printf("\nminor pentatonics\n");
                   minor_pentatonics(b);
                   break;
           case 3: // statements to display results
                   printf("\nmajor heptatonics\n");
                   major_heptatonics(b);
                   break;
           case 4: // statements to Save file
                   printf("\nminor heptatonics\n\n");
                   minor_heptatonics(b);
                   break;
           case 5: exit(0);
           default:  // should not happen!
                   printf("\nError!!!! %d\n", choice);
            }
       }
    return 0;
};