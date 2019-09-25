#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t, pres, location;
    string s;
    
    cin >> t;
    while(t--) {
        cin >> s;
        int arr[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        location = 0;
        for (int i =0; i < s.size(); i++) {
            cout << s[i] <<endl;
            pres = (int)s[i];
            pres = pres - 97;
            arr[pres]++;
        }

        int max = arr[0];
        cout << "max::::: " << max;
        for (int c = 1; c < 26; c++) {
            cout << "arr[" << c <<"] = " << arr[c] <<endl;
            if (arr[c] > max) {
                max = arr[c];
                location = c;
            }
        }
        location = location + 97;
        cout << "location:::: " << location <<endl;
        cout << (char)location << endl; 
    }
}
