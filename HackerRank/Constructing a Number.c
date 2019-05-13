#include <stdio.h>
int main()
{
    int t, n, a[100], m, s, i;
    s = 0;
    scanf("%d", &t);
    while (t > 0)
    {
        s = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
        }
        for (i = 0; i < n; i++)
        {

            while (a[i] > 0)
            {
                m = a[i] % 10;
                s = s + m;
                a[i] = a[i] / 10;
            }
        }
        if (s % 3 == 0)
        {
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
        }

        t--;
    }
    return 0;
}