#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Variable declarations

void print_menu() 
{
    char *ascii_art = "              .:~?5GB##&&&&##BG5?~:.     \n"
    "         .^JB&@@@@@@@@@@@@@@@@@@@@@@&BJ^.         \n"
    "      :J#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#J:      \n"
    "   .J&@@@@@@@@@@&GY?!~^^::^^~!?YG&@@@@@@@@@@&J.   \n"
    " ^B@@@@@@@@&G7:..^!J5GB####BG5J!^..:7G&@@@@@@@@B^ \n"
    "G@@@@@@@&Y: :?G&@@@@@@@@@@@@@@@@@@&B?:.:Y&@@@@@@@G\n"
    "#@@@@@B^ :5&@@@@@@@@@@@@@@@@@@@@@@@@@@&5: ^B@@@@@#\n"
    " ~YY?. !&@@@@@@@@@#P?!^^::^^!?P#@@@@@@@@@&! .?5Y~ \n"
    "      G@@@@@@@#?:.:~?5GBBBBG5?~:.:?#@@@@@@@G      \n"
    "      J@@@@@Y..!G&@@@@@@@@@@@@@@@B7..Y@@@@@J      \n"
    "       .~!^ :G@@@@@@@@@@@@@@@@@@@@@@G: ^~~.       \n"
    "           :@@@@@@@&BY?7777?YB&@@@@@@@:           \n"
    "            B@@@@G!!YB&@@@@&BY!!G@@@@#            \n"
    "             .^^.7&@@@@@@@@@@@@&7.^^.             \n"
    "                 5@@@@@7  7@@@@@5                 \n"
    "                  :G@@@@BB@@@@G:                  \n"
    "                    :P@@@@@@G:                    \n"
    "                      .5&&5.                      \n";
    printf("%s\n", ascii_art);
    printf("Welcome to the free Wi-Fi service!\n");

}

char random_char(int index)
{
    char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    return charset[index];
}

int main() 
{
    print_menu();
    char verbose_mode[10] = "OFF";
    char enable_verbose_mode[10];
    printf("Enable verbose mode? (Y/N) [Currently %s]: ", verbose_mode);

    // Prompt user to enable or disable verbose mode
    scanf("%s", enable_verbose_mode);
    if (strcmp(enable_verbose_mode, "Y") > 0)
    {
        printf("Sorry, verbose mode is only allowed for admins, which you are not. Sorry!\n");
    }
    else if (strcmp(enable_verbose_mode, "N") > 0)
    {
        printf("Verbose mode disabled!\n");
    }
    else 
    {
        printf("Invalid input!\n");
    }

    // Check if verbose mode is enabled
    if (strcmp(verbose_mode, "ON") == 0)
    {
        printf("Verbose mode has been enabled!\n");
        printf("Verbose Mode: [%s]\n", verbose_mode);
    }

    // Prompt user for password
    char check_password[20] = "FALSE";
    char password[10];
    char enter_password[10];
    printf("To access the free Wi-Fi, please enter the password! \n");
    while (strcmp(check_password, "TRUE") != 0)
    {
        printf("Password >>> ");
        scanf("%s", enter_password);
        if (strcmp(verbose_mode, "ON") == 0)
        {
            printf("\nPassword entered: %s\n", enter_password);
            printf("Password check: %s\n", check_password);
        }
        printf("Invalid Password!\n");
    }

    if (strcmp(verbose_mode, "ON") == 0)
    {
        printf("Password check successful!\n");
    }

    printf("Not so fast! Due to an increasing number of data breaches recently, we have implemented 2FA!\n");

    srand(time(NULL));
    char two_fa_code[18];

    int i, index;
    for (i = 0; i < 16; i++)
    {
        index = rand() % 62;
        two_fa_code[i] = random_char(index);
    }

    two_fa_code[i] = 'X'; // We do not forget '\0' for the string termination :D

    two_fa_code[i + 1] = '\0';

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    char enter_two_fa_code[64];


    if (strcmp(verbose_mode, "ON") == 0)
    {
        printf("%s\n", two_fa_code);
    }

    // Prompt user for 2FA code
    printf("Enter 2FA code: ");
    scanf("%s", enter_two_fa_code);

    // Check if 2FA code is correct
    if (strcmp(enter_two_fa_code, two_fa_code) == 0)
    {
        printf("2FA code check successful!\n");
    }

    else
    {
        printf("2FA code check failed!\n");
        printf("Exiting program...\n");
        exit(0);
    }

    char flag[64];
    char *flag_ptr = flag;
    FILE *file = fopen("flag.txt", "r");
    if (file == NULL)
    {
        printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
        exit(0);
    }

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("You have successfully logged in! To your free Wi-Fi! Enter anything to continue enjoying Internet!\n");
    char *input[10];
    // Infinite loop
    while (1)
    {
        scanf("%s", input);
        fgets(flag, sizeof(flag), file);
        printf("\n");
        printf(input);
        printf("\n");
    }
    
    return 0;
}