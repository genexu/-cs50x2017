#include <stdio.h>
#include <stdint.h>

typedef uint8_t  BYTE;

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: ./recover image");
        return 1;
    }

    char *infile = argv[1];
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    BYTE block[512];
    int picNum = 0;
    int found = 0;
    char outputFilename[9];
    FILE *outptr;
    while (fread(&block, 512, 1, inptr)) {
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] & 0xf0) == 0xe0) {
            if (found == 0) {
                found = 1;
            } else {
                fclose(outptr);
            }
            sprintf(outputFilename, "%03i.jpg", picNum);
            printf("Output file %s\n", outputFilename);
            outptr = fopen(outputFilename, "w");
            fwrite(block, sizeof(block), 1, outptr);
            picNum++;
        } else {
            if (found) {
                fwrite(block, sizeof(block), 1, outptr);
            }
        }
    }
    fclose(inptr);
}