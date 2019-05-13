#include <stdio.h>
int main()
{
    int n, a[10000], i;
    float x1, y1, z1, x, y, z;
    x = 0;
    y = 0;
    z = 0;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    i = 0;
    for (i = 0; i < n; i++)
    {
        if (a[i] > 0)
            x++;
        else if (a[i] < 0)
            y++;
        else
            z++;
    }
    x1 = x / n;
    y1 = y / n;
    z1 = z / n;
    printf("%f\n", x1);
    printf("%f\n", y1);
    printf("%f\n", z1);
    return 0;
}