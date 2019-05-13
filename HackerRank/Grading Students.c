#include <stdio.h>
int main()
{
    int n, grade, x, y;
    scanf("%d", &n);
    while (n > 0)
    {
        scanf("%d", &grade);
        x = grade / 5;
        y = 5 * (x + 1);

        if (y - grade < 3 && grade > 35)
            grade = y;
        printf("%d\n", grade);

        n--;
    }
    return 0;
}