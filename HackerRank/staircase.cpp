#include<iostream>
using namespace std;
int main()
{
    int n,i,j;
    cin>>n;
    for(i=0;i<n;i++)
    {
        for(j=0;j<=n-i-2;j++)
        {
            cout<<" ";
        }
        for(j=n-i-1;j<n;j++)
        {
            cout<<"#";
        }
        cout<<"\n";
    }
}