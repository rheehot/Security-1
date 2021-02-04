#include <stdio.h>

void main(){
    char a = 'a';
    char b = a >> 4;
    char c = (a << 4) & 0xf0;
    char d = b | c;
    printf("%x %c\n", a, a);
    printf("%x\n", b);
    printf("%x\n", c);
    printf("%x\n", d);
}