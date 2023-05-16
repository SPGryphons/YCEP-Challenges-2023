#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ascii_art() {
    puts("\n"
    "    ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▀▀▄   ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀▄ ▀▄      ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄\n"
    "   █  █   ▄▀ ▐ ▄▀ ▀▄ █     ▄▀ ▐ ▄▀   █ █   █  █  █  █ █ █     █  █   ▄▀ █      █ █    █  ▐ ▐  ▄▀   ▐ █    █\n"
    "   ▐  █▄▄▄█    █▄▄▄█ ▐ ▄▄▀▀     █▄▄▄▀  ▐   █  ▐  ▐  █  ▀█     ▐  █▄▄▄█  █      █ ▐   █       █▄▄▄▄▄  ▐    █\n"
    "      █   █   ▄▀   █   █        █   █      █       █   █         █   █  ▀▄    ▄▀    █        █    ▌      █\n"
    "     ▄▀  ▄▀  █   ▄▀     ▀▄▄▄▄▀ ▄▀▄▄▄▀   ▄▀▀▀▀▀▄  ▄▀   █         ▄▀  ▄▀    ▀▀▀▀    ▄▀        ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀\n"
    "    █   █    ▐   ▐          ▐ █    ▐   █       █ █    ▐        █   █             █          █    ▐     █\n"
    "    ▐   ▐                     ▐        ▐       ▐ ▐             ▐   ▐             ▐          ▐          ▐\n"
    "\n");
    printf("Welcome to the Hazbin Hotel! HAHAHAHAHAHA >:)\n");
    printf("We hope you enjoy your stay in HELL!\n");
}

int main() {
    char flag[64];
    char *flag_ptr = flag;
    FILE *file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
        exit(0);
    }
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    ascii_art();
    char secret_room_key[10] = "f7395e\0";
    char room_key[64];
    printf("Enter your room key: ");
    scanf("%s", room_key);
    fgets(flag, sizeof(flag), file);
    printf(room_key);
    if (strcmp(room_key, secret_room_key) == 0) {
        printf("\n");
        printf("Welcome to the secret room!\n");
        printf("flag: %s\n", flag_ptr);
    } else {
        printf("\n");
        printf("Wrong key! Get out of here!\n");
    }
    return 0;
}