#include <stdio.h>
int main()
{
    int i, d, m, n, s[10000], x, t, j;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d", &s[i]);
    scanf("%d", &d);
    scanf("%d", &m);
    for (i = 0; i < n - m + 1; i++)
    {
        t = 0;
        for (j = i; j < m + i; j++)
        {
            t = t + s[j];
        }
        if (t == d)
            x++;
    }
    printf("%d", x);
}