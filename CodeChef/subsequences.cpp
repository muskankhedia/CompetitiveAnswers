#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int printSubsequences(int arr[], int n, int k) 
{ 
    /* Number of subsequences is (2**n -1)*/
    unsigned int opsize = pow(2, n); 
  
    /* Run from counter 000..1 to 111..1*/
    int min = 10000, sum, count = 0;
    vector<int> g1; 
    for (int counter = 1; counter < opsize; counter++) 
    { 
        g1.clear();
        int l;
        for (int j = 0; j < n; j++) 
        { 
            /* Check if jth bit in the counter is set 
                If set then print jth element from arr[] */
            if (counter & (1<<j)) {
                // cout << arr[j] << " "; 
                g1.push_back(arr[j]);
            }
        } 
        l = g1.size();
        if (l == k) {
            sum = accumulate(g1.begin(),g1.end(),0);
            if (sum < min) {
                min = sum;
                count = 1;
            } 
            else if (sum == min) {
                count++;
            }
        } 
        
    } 
    return count;
} 


int main() {
	int t;
	cin>>t;
	while(t--)
	{
        int n, k;
        cin>>n>>k;
        int arr[n];
        for(int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        int c = printSubsequences(arr, n, k);
        cout<<c<<endl;
    }
}

