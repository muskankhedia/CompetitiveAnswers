#include<iostream>
using namespace std;
int main()
{
    int n,a[1000],i,p=0,q=0,r=0;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(i=0;i<n;i++)
    {
        if(a[i]>0)
            p++;
        else if(a[i]<0)
            q++;
        else
            r++;
    }
    cout<<(float)p/n<<"\n";
    cout<<(float)q/n<<"\n";
    cout<<(float)r/n<<"\n";
}