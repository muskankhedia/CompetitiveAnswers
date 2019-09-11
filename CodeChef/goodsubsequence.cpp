#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int printSubsequences(int arr[], int n, int k) 
{ 
    unsigned int opsize = pow(2, n); 
  
    int min = 10000,count = 0;
    vector<int> g1; 
    for (int counter = 1; counter < opsize; counter++) 
    { 
        g1.clear();
        int l;
        for (int j = 0; j < n; j++) 
        { 
            if (counter & (1<<j)) {
                g1.push_back(arr[j]);
            }
        } 
        
        l = g1.size();
        if (l <= k){
            auto it = std::unique(g1.begin(), g1.end());
            int x = ((it == g1.end()) ? 1 : 0);
            if (x == 1){
                 for(vector<int>::iterator i = g1.begin(); i != g1.end(); i++) 
                {
                    cout << *i <<" ";  
                }
                cout <<endl;
                count++;
            }
        }
    } 
    return count;
} 


int main() {
        int n, k;
        cin>>n>>k;
        int arr[n];
        for(int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        int c = printSubsequences(arr, n, k);
        cout<<c+1<<endl;
}

