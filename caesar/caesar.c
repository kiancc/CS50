#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string s);
char rotate(char c, int pos);

int main(int argc, string argv[])
{
    //checks if the right amount of arguments are passed and if it is a valid argument (digits only)
    if (argc == 2 && only_digits(argv[1]))
    {
        //converts argument to an integer key and asks for text that is to be ciphered
        int key = atoi(argv[1]);
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        //iterates through plaintext and prints the cipher of each character
        for (int i = 0; i < strlen(plaintext); i++)
        {
            char ciphertext = rotate(plaintext[i], key);
            printf("%c", ciphertext);
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

bool only_digits(string s)
{
    int len = strlen(s);
    int checker = 0;
    //iterates through string and counts how many times a digit appears
    for (int i = 0; i < len; i++)
    {
        if (isdigit(s[i]) != 0)
        {
            checker++;
        }
    }
    // returns true if the string length is the same as the number of digits, meaning that there are only digits in the string, otherwise false
    if (checker == len)
    {
        return true;
    }
    return false;
}

char rotate(char c, int k)
{
    //checks if c is alphabetic, if not just returns character
    if (isalpha(c))
    {
        //checks if lowercase
        if (islower(c))
        {
            //if key is greater than ASCII index of z, it will wrap around.
            if (k % 26 + c > 122)
            {
                c = c + ((k % 26) - 26);
            }
            else
            {
                c = c + (k % 26);
            }
            return c;
        }
        //checks if upper case
        if (isupper(c))
        {
            //if key is greater than ASCII index of Z, it will wrap around.
            if (k % 26 + c > 90)
            {
                c = c + ((k % 26) - 26);
            }
            else
            {
                c = c + (k % 26);
            }
            return c;
        }
    }
    return c;
}
