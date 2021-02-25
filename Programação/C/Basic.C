#include <stdio.h>
#include <stdlib.h>
#include <cstring>
int main(){
	char ip1[]={0},ip2[]={0},ip1xk[]={},ip2xk[]={};
	char cmd[256];
	bool listaip[100];
	int j,i,k,l,m;
	for (j=0;j<3;j++){
		for (i=0;i<=100;i++){
			ip1[10]=("10.10.%d.100",i);
			ip2[10]=("10.10.%d.200",i);
			ip1[10]=scanf("%s",ip1);
			ip2[10]=scanf("%s",ip2);
			printf("(%s)\n",ip1);
			for (k=0, k<strlen(ip1),k++){
				if (ip1[k]!=="."){
					ip1xk[k]=ip1[k];
				}else {
					for(l=k, l<strlen(ip1xk),l++){
						
						ipx1k[l]=ip1[k]
						ip1xk[l]=ip1[l++];

					}m=strlen(ip1xk);
					ipx1k[m]={};

				}
			}	
				/*if ip1[i]
				if (sprintf("ping -c 1 %s\n",ip1)==0){
					printf("%s pingou\n", ip1);
					return 1;
				}else{
					if (sprintf("ping -c 1 %s\n",ip2)==0){
						printf("%s pingou\n",ip2);
						return 1;
					}else {printf("%s e %s não pingaram\n",ip1,ip2 );
					return 0;}
				}

			}*/
		}
	}}
