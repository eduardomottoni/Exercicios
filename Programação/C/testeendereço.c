#include <stdio.h>
int main(){
	int a,b,c;
	int *p;
	char z[3000];
	float ba,zas;
	a=10;
	b=1;
	printf("%d\n",a );
	printf("%x\n",&a );
	printf("%d\n",b );
	printf("%x\n",&b );
	printf("%d\n",c );
	printf("%x\n",&c );
	p=&a;
	printf("%d\n",*p );
	printf("%x\n",&p );
	printf("%x\n",&ba );
	printf("%x\n",&z );
	printf("%x\n",&zas );
	
}
