#include <stdio.h>
int main()
{
    long long int a[100000], i, s;
    int n;
    scanf("%d", &n);
    s = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%llu", &a[i]);
        s = s + a[i];
    }
    printf("%llu", s);
    return 0;
}
