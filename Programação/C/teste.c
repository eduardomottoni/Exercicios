#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct ip
{
	char a[56];
	int b;
	char c[56];
	
};
int main()
{	char bstring[5], concatenadas[20];
	int testeip(char zzz.a, char bstring, char zzz.c){
		concatenadas = strcat(zzz.a, bstring, zzz.c);
		system("ping %s", concatenadas);
	}
	struct ip zzz;
	for (i=0,i<60,i++){
		zzz.a={"10.10."};
		zzz.b=i;
		zzz.c={".200"};
		itoa(zzz.b, bstring, 5);
		testeip(zzz.a,bstring, zzz.c);

	}
	}
