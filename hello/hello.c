#include <stdio.h>
#include <cs50.h>

int main(void)
{
    /*asks for users name and stores as a string*/
    string name = get_string("What's your name? ");
    /*returns greeting with users name*/
    printf("hello, %s\n", name);
}