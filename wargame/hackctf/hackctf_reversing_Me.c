#include <stdio.h>
#include <string.h>

int main(){
	int i;
	char *serial = "H`cjCUFzhdy^stcbers^D1_x0t_jn1w^r2vdrre^3o9hndes1o9>}";
	char answer[54];

	for(i = 0; i < strlen(serial); i++){
		answer[i] = serial[i] ^ (i % 2);
	}

	printf("Flag: %s\n", answer);

	return 0;
}
