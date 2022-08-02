#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // initialise average variable
    float average;
    // loops over pixels in image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // finds average of each colour in pixel then assigns average value to each pixel colour
            average = (image[i][j].rgbtGreen + image[i][j].rgbtBlue + image[i][j].rgbtRed) / 3.0;
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtBlue = round(average);
            image[i][j].rgbtRed = round(average);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //initialise variables to store sepia values calcualted by formula for each colour
    float sepiaRed;
    float sepiaGreen;
    float sepiaBlue;
    // loop over each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calculates sepia values
            sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            // if sepia values are greater than 255 set the value to 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            // assigns rounded sepia values to pixels
            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // swaps pixels around using trick from lecture
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    // copies image to copy array pixel by pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // initialise variables
            int count = 0;
            float sumR = 0;
            float sumG = 0;
            float sumB = 0;
            for (int k = i - 1; k < i + 2; k++)
            {
                for (int l = j - 1; l < j + 2; l++)
                {
                    // if index is at an edge or corner force next iteration
                    if (k < 0 || k > height - 1 || l < 0 || l > width - 1)
                    {
                        continue;
                    }
                    // sums values surrounding pixel at copy[i][j] whilst counting the amount of sums so we can find average
                    else
                    {
                        sumR += copy[k][l].rgbtRed;
                        sumG += copy[k][l].rgbtGreen;
                        sumB += copy[k][l].rgbtBlue;
                        count++;
                    }
                }
            }
            //assigns average to pixels
            image[i][j].rgbtRed = round(sumR / count);
            image[i][j].rgbtGreen = round(sumG / count);
            image[i][j].rgbtBlue = round(sumB / count);
        }
    }
    return;
}
