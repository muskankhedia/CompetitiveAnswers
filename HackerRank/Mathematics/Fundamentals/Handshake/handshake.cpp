#include <stdio.h>
int main()
{
    int i, t, x[10000], a[10000];
    scanf("%d", &t);
    for (i = 0; i < t; i++)
    {
        scanf("%d", &a[i]);
        x[i] = a[i] * (a[i] - 1) / 2;
    }
    for (i = 0; i < t; i++)
    {
        printf("%d\n", x[i]);
    }
    return 0;
}