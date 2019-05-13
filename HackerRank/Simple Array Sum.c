#include <stdio.h>
int main()
{
    int i, n, a[10000], s;
    s = 0;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        s = s + a[i];
    }
    printf("%d", s);
    return 0;
}