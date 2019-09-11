#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t,n, nextTerm;
	cin>>t;
	while(t--)
	{
        cin>>n;
        vector<int> arr;

        arr.push_back(0);
        arr.push_back(1);
        for (int i = 1; i < n-1; i++) {
            nextTerm = arr[i-1] + arr[i];
            nextTerm = nextTerm % 10;
            arr.push_back(nextTerm);
        }
        if (n > 7) {

            for(vector<int>::iterator i = arr.begin(); i != arr.end(); i++) 
            {
                cout << *i <<" ";   // for printing the vector
                *i = *i % 10;

            }
            cout << endl;

        } 

        while(arr.size() > 1) {
            int j = 0;
            for(vector<int>::iterator i = arr.begin(); i != arr.end(); i++) 
            {
                if (j % 2 == 0) {
                    arr.erase(i);
                    // cout<<*i;
                    i--;
                }
                j++;
                cout<<"J::::"<<j<<endl;
                for(vector<int>::iterator i = arr.begin(); i != arr.end(); i++) 
                {
                    cout << *i <<" ";   // for printing the vector
                    *i = *i % 10;

                }
                cout << endl;
            }
            cout << endl;
        cout<<"reached";
        }
        cout<<arr[0]<<endl;
       
    }
}

// #include <iostream>
// #include <vector>
// #include <bits/stdc++.h>

// using namespace std;

// // function to evaluate logarithm base-10 
// double value2(double d) 
// { 
// 	return log2(d); 
// } 

// int main() {
// 	int t;
//     double n;
// 	cin>>t;
// 	while(t--)
// 	{
//         cin>>n;
//         double exp = value2(n);
//         int res = floor(exp);

//         if (res == 0 || res == 1 || res == 2 || res == 3) {
//             cout<<res<<endl;
//         } else if (res%4 == 0) {
//             cout<<"0"<<endl;
//         } else if (res%4 == 1) {
//             cout<<"9"<<endl;
//         } else if (res%4 == 2) {
//             cout<<"2"<<endl;
//         } else if (res%4 == 3) {
//             cout<<"3"<<endl;
//         } else {
//             cout<<"Invalid Input"<<endl;
//         }
       
//     }
// }

// #include <iostream>
// #include <vector>
// #include <bits/stdc++.h>

// using namespace std;

// // function to evaluate logarithm base-10 
// long long int value2(long long int d) 
// { 
// 	return log2(d); 
// } 

// int main() {
// 	long long int t;
//     long long int n;
// 	cin>>t;
// 	while(t--)
// 	{
//         cin>>n;
//         double exp = value2(n);
//         long long int res = floor(exp);

//         if (res == 0 || res == 1 || res == 2 || res == 3) {
//             cout<<res<<endl;
//         } else if (res%4 == 0) {
//             cout<<"0"<<endl;
//         } else if (res%4 == 1) {
//             cout<<"9"<<endl;
//         } else if (res%4 == 2) {
//             cout<<"2"<<endl;
//         } else if (res%4 == 3) {
//             cout<<"3"<<endl;
//         } else {
//             cout<<"Invalid Input"<<endl;
//         }
       
//     }
// }