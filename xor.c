//encode a input file with XOR with key { 0xe6, 0x6f }

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    FILE *fp2;
    char *buffer;
    char *buffer2;
    int i;
    int size;
    int size2;
    int key[2] = { 0xe6, 0x6f }; // change this as needed

    if (argc != 3)
    {
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        exit(1);
    }

    fp = fopen(argv[1], "rb");
    if (fp == NULL)
    {
        printf("Cannot open %s\n", argv[1]);
        exit(1);
    }

    fp2 = fopen(argv[2], "wb");
    if (fp2 == NULL)
    {
        printf("Cannot open %s\n", argv[2]);
        exit(1);
    }

    fseek(fp, 0, SEEK_END);
    size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    buffer = (char *)malloc(size);
    buffer2 = (char *)malloc(size);

    fread(buffer, size, 1, fp);

    for (i = 0; i < size; i++)
    {
        buffer2[i] = buffer[i] ^ key[i % 2];
    }

    fwrite(buffer2, size, 1, fp2);

    fclose(fp);
    fclose(fp2);
    free(buffer);
    free(buffer2);

    return 0;
}
