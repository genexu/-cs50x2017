#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "bmp.h"

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }
    float n = atof(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];

    if (n < 0 || n > 100) {
        fprintf(stderr, "n: %f; n should between 0 to 100\n", n);
        return 1;
    }

    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL) {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL) {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 1;
    }

    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || bi.biBitCount != 24 || bi.biCompression != 0) {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    BITMAPINFOHEADER outfileBi;
    outfileBi = bi;
    outfileBi.biWidth = bi.biWidth * n;
    outfileBi.biHeight = bi.biHeight * n;

    int infilePadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int outfilePadding = (4 - (outfileBi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    outfileBi.biSizeImage = (outfileBi.biWidth * sizeof(RGBTRIPLE) + outfilePadding) * abs(outfileBi.biHeight);

    BITMAPFILEHEADER outfileBf;
    outfileBf = bf;
    outfileBf.bfSize = 54 + (abs(outfileBi.biWidth) * abs(outfileBi.biHeight) * 3) + abs(outfileBi.biHeight) * outfilePadding;

    fwrite(&outfileBf, sizeof(BITMAPFILEHEADER), 1, outptr);
    fwrite(&outfileBi, sizeof(BITMAPINFOHEADER), 1, outptr);
    int jump = 1;
    if (n < 1) {
        jump = round(1/n);
    }
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i+=jump) {
        RGBTRIPLE *tripleArray = malloc(outfileBi.biWidth * sizeof(RGBTRIPLE));
        if (n >= 1) {
            for (int j = 0; j < bi.biWidth; j++) {
                RGBTRIPLE triple;
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                for (int k = 0; k < n; k ++) {
                    tripleArray[(int)round((j*n))+k] = triple;
                }
            }
        }
        else {
            for (int j = 0; j < outfileBi.biWidth; j++)
            {
                RGBTRIPLE triple;
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                tripleArray[j] = triple;
                fseek(inptr, sizeof(RGBTRIPLE) * ((1/n) - 1), SEEK_CUR);
            }
            for (int j = 0; j < ((1/n) - 1); j++) {
                fseek(inptr, bi.biWidth * sizeof(RGBTRIPLE), SEEK_CUR);
                fseek(inptr, infilePadding, SEEK_CUR);
            }
        }

        fseek(inptr, infilePadding, SEEK_CUR);

        for (int j = 0; j < n; j ++) {
            fwrite(tripleArray, sizeof(RGBTRIPLE), abs(outfileBi.biWidth), outptr);
            for (int k = 0; k < outfilePadding; k++) {
                fputc(0x00, outptr);
            }
        }
        free(tripleArray);
    }

    fclose(outptr);
    fclose(inptr);

    return 0;
}