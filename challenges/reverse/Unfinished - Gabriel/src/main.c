#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <unistd.h>
#include <signal.h>


/* xorshift128+ implementation copied from wiki */
struct xorshift128p_state {
	uint64_t x[2];
};

/* The state must be seeded so that it is not all zero */
uint64_t xorshift128p(struct xorshift128p_state *state)
{
	uint64_t t = state->x[0];
	uint64_t const s = state->x[1];
	state->x[0] = s;
	t ^= t << 23;		// a
	t ^= t >> 18;		// b -- Again, the shifts and the multipliers are tunable
	t ^= s ^ (s >> 5);	// c
	state->x[1] = t;
	return t + s;
}

#define ARRLEN(x) sizeof(x)/sizeof(x[0])
void win(int x, int y) {
	struct xorshift128p_state state;
	state.x[0] = x;
	state.x[1] = y;
	unsigned int index[] = { 217, 148, 168, 104, 254, 150, 43, 413, 186, 299, 154, 30, 542, 982, 159, 83, 354, 239, 36, 47, 243, 663, 5, 154, 101, 156, 94, 264, 42, 155, };
	for(unsigned int i = 0; i < ARRLEN(index); i++) {
		char val = 0;
		for(unsigned int j = 0; j < index[i]; j++) {
			val = xorshift128p(&state) & 0xff;
		}
		putchar(val);
	}
	puts("");
}

void start() {
	time_t s0 = time(NULL);
	time_t s1;
	struct xorshift128p_state xors128p;
	xors128p.x[0] = 0xf1; //all we do is lalalalalalalalaala
	xors128p.x[1] = 0x1f;
	printf("Where do you wanna go?\n");
	printf("Please enter the x,y values here\n>> ");
	int x, y;
	int realx, realy;
	scanf("%d,%d", &x, &y);
	if((x < -100 || x > 100) || (y < -100 || y > 100)) {
			puts("Enter values between -100 and 100");
			return;
	}
	printf("heading to %d,%d\n", x, y);
	s1 = time(NULL);
	if((s1 - s0) > 10) {
		printf("Insert Angry Noises Here");
		return;
	}
	realx = (xorshift128p(&xors128p) % 201) - 100;
	realy = (xorshift128p(&xors128p) % 201) - 100;
	if(x == realx && y == realy) { 
		printf("Insert Interesting Find Here\n");
		win(x, y);
	} else
		printf("Insert Invalid Text Here\n");
}

int main() {
	printf("Welcome Insert User Here!\nWelcome to Insert Game Here. The winner is the first to reach Insert Goal Here!\n");
	puts("Are you ready?");
	printf("Insert Prompt Here ");
	char prompt = 0x00;
	fread(&prompt, 1, 1, stdin);
	if(prompt != 'y' && prompt != 'Y') {
		printf("Goodbye!\n");
		return 0;
	}
	printf("Insert Starting Message Here\n");
	start();
	return 0;
}
