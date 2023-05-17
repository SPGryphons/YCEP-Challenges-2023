#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define BUFMAX 64

/*
 ▄  █ ██   █ ▄▄  █ ▄▄ ▀▄    ▄     ▄  █ ████▄    ▄▄▄▄▀ ▄███▄   █      ▄
█   █ █ █  █   █ █   █  █  █     █   █ █   █ ▀▀▀ █    █▀   ▀  █     █
██▀▀█ █▄▄█ █▀▀▀  █▀▀▀    ▀█      ██▀▀█ █   █     █    ██▄▄    █    █
█   █ █  █ █     █       █       █   █ ▀████    █     █▄   ▄▀ ███▄ █
   █     █  █     █    ▄▀           █          ▀      ▀███▀       ▀
  ▀     █    ▀     ▀               ▀                               ▀
       ▀
*/

void ascii_art()
{
    puts("\n"
         " ▄  █ ██   █ ▄▄  █ ▄▄ ▀▄    ▄     ▄  █ ████▄    ▄▄▄▄▀ ▄███▄   █      ▄\n"
         "█   █ █ █  █   █ █   █  █  █     █   █ █   █ ▀▀▀ █    █▀   ▀  █     █\n"
         "██▀▀█ █▄▄█ █▀▀▀  █▀▀▀    ▀█      ██▀▀█ █   █     █    ██▄▄    █    █\n"
         "█   █ █  █ █     █       █       █   █ ▀████    █     █▄   ▄▀ ███▄  █\n"
         "   █     █  █     █    ▄▀           █          ▀      ▀███▀        ▀\n"
         "  ▀     █    ▀     ▀               ▀                               ▀\n"
         "       ▀\n");
}

void display_message()
{
    printf("Welcome to the Happy Hotel, where your dreams come true!\n");
    printf("We have a wide variety of rooms, from the standard room to the presidential suite!\n");
    printf("But before you check in with us, we need to know your ID to see which room you have been assigned to!\n");
}

void print_flag()
{
    char flag[BUFMAX];
    FILE *fptr;
    if ((fptr = fopen("flag.txt", "r")) == NULL)
    {
        printf("Error! opening file!");
        exit(1);
    }
    fgets(flag, BUFMAX, fptr);
    printf("Here is your flag: %s\n", flag);
    fclose(fptr);
}

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    ascii_art();
    display_message();
    char userid[20];
    char password[BUFMAX];
    char correct_password[20] = "qwerty";
    char another_userid[20] = "H001";
    char correct_userid[20] = "H100";
    printf("Please enter your ID (Format: HXXX) => ");
    gets(userid);
    if (strcmp(userid, correct_userid) == 0)
    {
        printf("Please enter your password => ");
        gets(password);
        if (strcmp(password, correct_password) == 0)
        {
            printf("Welcome back, %s! Your room number is HH-2345\n", userid);
        }
        else
        {
            int check_flag = strcmp(userid, another_userid);
            if (check_flag == 0)
            {
                printf("Welcome back, %s! Your room number is HH-5344\n", another_userid);
                print_flag();
            }
            else
            {
                printf("Sorry, %s, incorrect password!\n", userid);
            }
        }
    }
    else
    {
        printf("Incorrect ID!\n");
    }

    return 0;
}
