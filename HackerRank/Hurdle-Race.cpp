#include <stdio.h>
int main()
{
    int i, n, h, a[10000], max;
    scanf("%d", &n);
    scanf("%d", &h);
    max = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        if (a[i] > max)
            max = a[i];
    }

    if (h < max)
        printf("%d", max - h);
    else
        printf("0");
    return 0;
}