#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <stdlib.h>

void ignore_me_innit_buffering() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}


uint32_t xorshift32(uint32_t x) {
	x ^= x << 13;
	x ^= x >> 17;
	x ^= x << 5;
	return x;
}

char *option[] = {
	"Fraction",
	"Monkey",
	"Peaches",
	"Random",
	"Alden",
	"pneumonoultramicroscopicsilicovolcanoconiosis",
	"syzygy",
	"bloviate",
	"calligraphy"
};

int main() {
	ignore_me_innit_buffering();

	char input[500];
	int count = 0;
	uint32_t rng = time(NULL);
	FILE *fp;
	char flagbuf[100];

	puts("Lets play a Guessing game! I shall think of a word. Can you guess it correctly?\n");
	puts("Lets start! I'm thinking of a word...");
	printf(">> ");
	rng = xorshift32(rng);
	while(count < 64) {
		fgets(input, 500, stdin);
		if(strstr(input, option[rng % 9]) == NULL) {
			fprintf(stdout, "Sorry! I was thinking about %s!", option[rng % 9]);
			exit(0);
		}
		puts("Correct! Next word!");
		printf(">> ");
		count++;
		rng = xorshift32(rng);
	}

	fp = fopen("flag.txt", "r");
	if(fp == NULL) {
		puts("flag.txt not found, please run on the server, or contact the support team.");
		exit(0);
	}
	fgets(flagbuf, 100, fp);
	puts(flagbuf);
	fclose(fp);
	return 0;
}
