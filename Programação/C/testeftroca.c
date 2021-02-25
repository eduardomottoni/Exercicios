#include <stdio.h>
void troca(int a, int b){
	int temp;
	temp = a;
	a = b;
	b = temp;
	printf("%d=a, %d=b, %d=temp\n",a,b,temp );

}
int main(){
	int a,b,temp;
	a=3;
	b=2;
	troca(a,b);

	printf("%d=a e %d=b e %d=temp\n",a,b,temp );
}