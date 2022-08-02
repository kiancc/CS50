#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    int k = 0;
//Takes integer input for numbers between 1 and 8, re-prompts if not
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);
//Sets count as input given
    int count = n;

    while (n > k)
    {
        //prints empty space for "count" amount of times decreasing
        for (int l = count; l > 1; l--)
        {
            printf(" ");
        }
        //prints pyramid for "k" amount of times increasing on the left
        for (int j = 0; j <= k; j++)
        {
            printf("#");
        }
        //prints empty space to separate both pyramids by two white spaces
        printf("  ");
        //prints pyramid for "k" amount of times increasing on the right
        for (int m = k; m >= 0; m--)
        {
            printf("#");
        }
        //increases k and decreases count each iteration
        k++;
        count--;
        printf("\n");
    }
}


