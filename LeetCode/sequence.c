// #include <stdio.h>
// #include <string>
// #include <iostream>
// #include <iterator>
// #include <unordered_set>
// #include <cstring>

// using namespace std;

// int check(char checkStr, string t, int pos ){
//     bool found = false;
//     for(int i = pos; i < t.length(); i++) {
//         if (checkStr == t[i]) {
//             found = true;
//             pos = i;
//             break;
//         }
//     }
//     if(!found) {
//         pos = -1;
//     }
//     return pos;
// }

// int main()
// {
//     string s, t;
//     s = "abc";
//     t = "ahbgdc";
//     int pos = 0;
//     for (int i = 0; i < s.length(); i++) {
//         pos = check(s[i],t,pos);
//         if (pos == -1){
//             printf ("1");
//         }
//     }
//     printf("0");
//     return 0;
// }

bool isSubsequence(string s, string t) {
    int ls = s.length(), lt = t.length();
    int last = 0;
    for(int i=0;i<ls;i++) {
        bool match = false;
        for(int j=last;j<lt;j++){
            if (s[i]==t[j]) {
                match = true;
                last = j+1;
                break;
            }
        }
        if (!match) {
            return false;
        }
    }
    return true;
}
