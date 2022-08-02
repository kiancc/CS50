#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    int k = 0;
/*Takes integer input for numbers between 1 and 8, re-prompts if not */
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);

    int count = n;

    while (n > k)
    {
        for (int l = count; l > 1; l--)
        {
            printf(" ");
        }
        for (int j = 0; j <= k; j++)
        {
            printf("#");
        }
        k++;
        count--;
        printf("\n");
    }
}
