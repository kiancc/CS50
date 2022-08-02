#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//function's protoypes
int count_letters(string text);
int count_words(string text);
int sentence_count(string text);

int main(void)
{
    //gets user input
    string n;
    n = get_string("Text: ");
    //gets lengths for letters, words and sentences an assignes to corresponding integer variables
    float letter_length = count_letters(n);
    float word_length = count_words(n);
    float sentence_length = sentence_count(n);
    //calculates Coleman-Liau index
    float L = (letter_length / word_length) * 100;
    float S = (sentence_length / word_length) * 100;
    float index = (0.0588 * L) - (0.296 * S) - 15.8;
    int grade = round(index);
    //prints grade according to conditions
    if (grade < 1)
    {
        printf("Before Grade 1");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+");
    }
    else
    {
        printf("Grade %d", grade);
    }
    printf("\n");
}

int count_letters(string text)
{
    int count = 0;
    int len = strlen(text);
    //loop to count how many alphabetic characters there are in a string
    for (int i = 0; i < len; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(string text)
{
    int count = 0;
    int len = strlen(text);
    //loop to count how many white spaces there are in a sentence, which indicates a new word
    for (int i = 0; i < len; i++)
    {
        if (isspace(text[i]))
        {
            count++;
        }
    }
    //returns count + 1 due to the fact that there is always a word after the last whitespace
    return count + 1;
}

int sentence_count(string text)
{
    int count = 0;
    int len = strlen(text);
    //loop to count how many period, question marks or exclamation marks there are, indicating a new sentence.
    for (int i = 0; i < len; i++)
    {
        if (strchr(".?!", text[i]))
        {
            count++;
        }
    }
    return count;
}