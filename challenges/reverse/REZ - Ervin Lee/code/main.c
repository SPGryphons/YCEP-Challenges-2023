#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char input[50];
    char* magic_word = "n33D_h3aL1nG";
    printf("Someone one-tapped you on the head and you died.\n");
    printf("Can you say the magic word so that Sage can revive you? ");
    scanf("%s", &input);
    int x = strcmp(input, magic_word);
    if (x == 0) {
        printf("YOUR DUTY IS NOT OVER! YCEP2023{R3V3r53_3n9in33rin9_15_3Z} \n");
    } else {
        printf("That is not the magic word! Sage revived her Jett instead :(\n");
    }
    
    return 0;
}