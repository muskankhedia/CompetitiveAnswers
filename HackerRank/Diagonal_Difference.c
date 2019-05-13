#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n, a[100][100], x, y, i, j, z, z1;
    x = 0;
    y = 0;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
            scanf("%d", &a[i][j]);
    }
    for (i = 0; i < n; i++)
    {

        for (j = 0; j < n; j++)
        {
            if (i == j)
                x = x + a[i][j];
        }
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if ((i + j) == (n - 1))
                y = y + a[i][j];
        }
    }
    z = x - y;
    z1 = abs(z);
    printf("%d", z1);
    return 0;
}