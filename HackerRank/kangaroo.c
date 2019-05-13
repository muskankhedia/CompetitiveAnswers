#include <stdio.h>
int main()
{
    int x1, v1, x2, v2, m, i, y1, y2;
    scanf("%d", &x1);
    scanf("%d", &v1);
    scanf("%d", &x2);
    scanf("%d", &v2);
    m = 0;
    for (i = 0; i < 100000; i++)
    {
        y1 = x1 + (i * v1);
        y2 = x2 + (i * v2);
        if (y1 == y2)
            m++;
    }
    if (m >= 1)
        printf("YES");
    else
        printf("NO");
    return 0;
}