#include <stdio.h>
int main()
{
    int n, h[100000], i, y, temp;
    y = 0;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &h[i]);
    }
    temp = h[0];
    for (i = 1; i < n; i++)
    {
        if (h[i] > temp)
            temp = h[i];
    }
    for (i = 0; i < n; i++)
    {
        if (temp == h[i])
            y++;
    }

    printf("%d", y);
    return 0;
}