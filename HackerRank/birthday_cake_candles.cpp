#include<iostream>
using namespace std;
int main()
{
    long long a[1000000],n,max;
    int i,count=0;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    max=a[0];
    for(i=0;i<n;i++)
    {
        
        if(a[i]>max)
            max=a[i];
    }
    for(i=0;i<n;i++)
    {
        if(a[i]==max)
            count++;
    }
    cout<<count;
    return 0;
}