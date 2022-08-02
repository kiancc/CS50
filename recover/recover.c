#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    const int BLOCK_SIZE = 512;
    // Throws error if not exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    // Remember filenames
    char *infile = argv[1];

    // Open input file
    FILE *raw_file = fopen(infile, "r");
    if (raw_file == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }
    // defines type BYTE
    typedef uint8_t BYTE;
    // creates buffer variable
    BYTE buffer[BLOCK_SIZE];
    // create digit variable
    int digit = 0;
    // creates empty char array for filename
    char c[8];
    // creates empty output file
    FILE *out_file = NULL;

    while (fread(buffer, 1, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        // Checks for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // prints file name for each file found
            if (digit < 10)
            {
                sprintf(c, "00%i.jpg", digit);
            }
            else
            {
                sprintf(c, "0%i.jpg", digit);
            }
            out_file = fopen(c, "w");
            digit++;
        }
        if (out_file != NULL)
        {
            // keep writing if jpeg header is already found
            fwrite(buffer, 1, BLOCK_SIZE, out_file);
        }
    }
    fclose(out_file);
    fclose(raw_file);
}