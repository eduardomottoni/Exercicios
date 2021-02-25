
#include <stdio.h>

int mult(int x, int y){
	if (y==1){
		return x;
	} else { 
		return (x + mult(x, y-1));
	}
}

void main(){
	int a,b;
	printf("digita a\n");
	scanf("%d",a);
	printf("digita b\n");
	scanf("%d",b);
	printf("%d = a, %d = b, e a multiplicação dos dois termos é igual a %d.\n" ,a , b,mult(a,b));
}