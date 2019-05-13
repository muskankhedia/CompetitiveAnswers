#include <stdio.h>
int main()
{
    long long int a[5], i, s[5], n, j, temp;
    n = 5;
    for (i = 0; i < n; i++)
        scanf("%llu", &a[i]);
    for (i = 0; i < n; i++)
    {
        s[i] = 0;
        for (j = 0; j < n; j++)
        {
            if (j != i)
                s[i] = s[i] + a[j];
        }
    }
    for (i = 0; i < 5; i++)
    {
        for (j = i + 1; j < 5; j++)
        {
            if (s[i] > s[j])
            {
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
    printf("%llu %llu", s[0], s[n - 1]);
    return 0;
}