#include <stdio.h>
int main()
{
    int a[3], b[3], i, x, y;
    x = 0;
    y = 0;
    for (i = 0; i < 3; i++)
        scanf("%d", &a[i]);
    for (i = 0; i < 3; i++)
        scanf("%d", &b[i]);
    for (i = 0; i < 3; i++)
    {
        if (a[i] > b[i])
            x++;
        else if (a[i] < b[i])
            y++;
    }
    printf("%d %d", x, y);
    return 0;
}