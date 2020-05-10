class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        vector<int> check;
        int i;
        int x = 0;
        vector <int> now;
        for (i = 1; i <= N; i++) {
            check.push_back(i);
        }
        for (i = 0; i < trust.size(); i++) {
            now = trust.at(i);
            if (std::find(check.begin(), check.end(), now[0]) != check.end()) {
                check.erase(std::find(check.begin(), check.end(), now[0]));
            } 
        }
        if (check.size() == 1) {
            for (i = 0; i < trust.size(); i++){
                if (trust[i][1] == check[0])
                    x++;
            }
            if (x == N-1)
                return check[0];
            else
                return -1;
        } else {
            return -1;
        }
    }
};
