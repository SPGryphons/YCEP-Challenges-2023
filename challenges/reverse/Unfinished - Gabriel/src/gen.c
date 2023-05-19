#include <stdio.h>
#include <stdint.h>

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

int main() {
	char flag[] = "YCEP2023{g01ng_0n_A_tr1P_n0w}";
	struct xorshift128p_state state;
	state.x[0] = 0xf1;
	state.x[1] = 0x1f;
	int x = (xorshift128p(&state) % 201) - 100;
	int y = (xorshift128p(&state) % 201) - 100;
	struct xorshift128p_state xors128p;
	xors128p.x[0] = x;
	xors128p.x[1] = y;
	printf("x: %d, y: %d\n", x, y);
	printf("unsigned int index[] = { ");
	for(int i = 0; i < ARRLEN(flag); i++) {
		unsigned int count = 0;
		char val = 0;
		do {
			val = xorshift128p(&xors128p) & 0xff;
			count++;
		}while(val != flag[i]);
		printf("%d, ", count);
	}
	printf("};\n");
	return 0;
}
