#include <stdio.h>
int main()
{
    int n, k, arr[10000], i, j, m, s;
    scanf("%d", &n);
    scanf("%d", &k);
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    m = 0;
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            s = arr[i] + arr[j];
            if (s % k == 0)
                m++;
        }
    }
    printf("%d", m);
    return 0;
}