#include <stdio.h>
#include <string.h>
#include <ctype.h>

void decrypt(char* str) {
    int strLength = strlen(str);

    //Reverse the string
    int left = 0;
    int right = strLength - 1;
    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }

    //-2 Ascii for alphanum
    for (int i = 0; i < strLength; i++) {
        if (isalnum(str[i])) {
            str[i] -= 2;
        }
    }
}

int main() {
    char encrypted[] = "n22e_7k_Gf2e_ipkutGx5t";
    
    //Decrypt string
    decrypt(encrypted);
    printf("Decrypted string: %s\n", encrypted);

    return 0;
}