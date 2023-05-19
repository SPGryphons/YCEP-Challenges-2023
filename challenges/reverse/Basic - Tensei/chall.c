#include <stdio.h>
#include <string.h>
#include <ctype.h>

void encrypt(char* str) {
    int strLength = strlen(str);

    //+2 Ascii for alphanums
    for (int i = 0; i < strLength; i++) {
        if (isalnum(str[i])) {
            str[i] += 2;
        }
    }

    //Reverse string
    int left = 0;
    int right = strLength - 1;
    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }
}

int main() {
    char secret[] = "Input Flag Here";

    // Encrypt string
    encrypt(secret);
    printf("Encrypted string: %s\n", secret);

    return 0;
}
