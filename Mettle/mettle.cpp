// #include <iostream>
// #include <iterator>
// #include <unordered_set>
// #include <vector>
// #include <bits/stdc++.h>
// #include <algorithm>
// 
// using namespace std;
// 
// int main() {
// 
    // return 0;
// }


#include<stdio.h>
void merge(int *a,int start,int mid,int end)
{
    int p=start,q=mid+1;
    int arr[end-start+1],k=0;
    for(int i=start;i<=end;i++){
        if(p>mid)
         arr[k++]=a[q++];
        else if(q>end)
         arr[k++]=a[p++];
        else if(a[p]>a[q])
         arr[k++]=a[p++];
         else
          arr[k++]=a[q++];
    }
    for(p=0;p<k;p++)
     a[start++]=arr[p];
}
void merge_sort(int *a,int start,int end)
{
    if(start<end){
        int mid=(start+end)/2;
        merge_sort(a,start,mid);
        merge_sort(a,mid+1,end);
        merge(a,start,mid,end);
    }
}

int main()
{
    int n;
    scanf("%d %d",&n);
    int a[n];
    for(int i=0;i<n;i++)
     scanf("%d",&a[i]);
     merge_sort(a,0,n-1);
//     for(int i=0;i<n;i++)
  //    printf("%d ",a[i]);
     for(int i=0;i<n-1;i++){
      if(((a[i]+a[i+1]+a[i+2])%a[i]==0 && (a[i]+a[i+1]+a[i+2])%a[i+1] !=0 && (a[i]+a[i+1]+a[i+2])%a[i+2]!=0) || 
        ((a[i]+a[i+1]+a[i+2])%a[i]!=0 && (a[i]+a[i+1]+a[i+2])%a[i+1] ==0 && (a[i]+a[i+1]+a[i+2])%a[i+2]!=0) ||
        ((a[i]+a[i+1]+a[i+2])%a[i]!=0 && (a[i]+a[i+1]+a[i+2])%a[i+1] !=0 && (a[i]+a[i+1]+a[i+2])%a[i+2]==0))
         {
          printf("%d ",a[i]+a[i+1]+a[i+2]);
          return 0;
      }
     }
     printf("-1");
     return 0;
}