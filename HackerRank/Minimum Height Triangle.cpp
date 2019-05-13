#include <stdio.h>
#include <math.h>
int main()
{
    float a, b;
    float h;
    scanf("%f", &b);
    scanf("%f", &a);
    h = 2 * a / b;
    int x;
    x = (int)h;
    if ((h - x) > 0)
        x++;
    printf("%d", x);
    return 0;
}