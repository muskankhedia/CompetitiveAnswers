#include <stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    int t,i,sum,j,space,l;
    int ht1[26]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25};
    int ht2[26]={36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61};
    int ht3[10]={35,26,27,28,29,30,31,32,33,34};
    char *c;
    scanf("%d",&t);
    getchar();
    while(t>=1)
    {
    	j=0;
        sum=0;
        space=0;
        c=(char*)calloc(700,sizeof(char));
        gets(c);
        l=strlen(c);
        for(i=0;i<l;i++)
        {
            if(c[i]==' ')
            {
            	space++;
            	j=0;
            }
            else if(c[i]>='A'&&c[i]<='Z')
            {
            	sum=sum+j+ht2[c[i]-65];
            	j++;
            }
            else if(c[i]>='a'&&c[i]<='z')
            {
			    sum=sum+j+ht1[c[i]-97];
			    j++;
			}
            else if(c[i]>='0'&&c[i]<='9')
            {
            	sum=sum+j+ht3[c[i]-48];
            	j++;
            }
        }
        printf("%d\n",(space+1)*sum);
        t--;
        free(c);
    }
    return 0;
}