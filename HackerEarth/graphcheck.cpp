#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    bool mat[n][n];
    for(int i = 0;i < n;++i)
        for(int j = 0;j < n;++j)
            A[i][j] = false;
    
    int a, b, nq, q1, q2;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        mat[a][b] = true;
        mat[b][a] = true;
    }

    for (int i = 0; i < q; i++) {
        cin >> q1 >> q2;
        if (mat[q1][q2]) {
            cin >> "YES";
        } else {
            cin >> "NO";
        }
    }
    return 0;

}