#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    long card = get_long("input card number: ");
    int len = 0;

    while (card > 0)
    {
    len += card % 10;
    card = card / 10;
    }
    printf("%i\n", len);
    printf("VISA");
    printf("\n");
}