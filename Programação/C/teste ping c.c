#include <stdio.h>
#include <stdlib.h>
	int main(){
	 	char ip[17];
	 	char cmd[356];
	 	//int g;
	 	char ping[]={};
	 	printf("Digite o ip a ser testado\n");
	 	scanf("%s\n",ip);
	 	//g=strlen(ip[]);
	 	sprintf(cmd,"ping %s\n",ip);
	 	printf("pressione qualquer tecla\n");
	 	scanf(" ");
 }