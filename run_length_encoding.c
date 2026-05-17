#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


void decompress(FILE *infile, FILE *outfile)
{
   while (true)
   {
	   int c = getc(infile);
	   if (c == EOF){
		   break;
	   }
	   int the_count = getc(infile);

	   for (int i=0; i<the_count; i++)
	   {
		   putc(c,outfile);
	   }
   }
}

void compress(FILE *infile, FILE *outfile)
{

	int seen = fgetc(infile);
	int repeat_count = 1;
	int next_char;

	while ((next_char = fgetc(infile)) != EOF)
	{
	
		if (next_char == seen)
		{
			repeat_count++;

			if (repeat_count >= 255)
			{

			
			putc(seen, outfile);
			putc(repeat_count, outfile);
			repeat_count = 0;

			}

		}
		else
		{
			putc(seen, outfile);
			putc(repeat_count, outfile);
			repeat_count = 1;
			seen = next_char;
		}
	
	}
			putc(seen, outfile);
			putc(repeat_count, outfile);
			putchar(seen);
			putchar(repeat_count);
		
}


int main(int argc, char *argv[])
{
	if (argc != 4)
	{
		printf("Argument count error.\n Usage %s [compress|decompress] infile outfile\n", argv[0]);
		exit(-1);
	}


         FILE *infile = fopen(argv[2], "r");
         FILE *outfile = fopen(argv[3], "w");
	 if (infile == NULL){
		 printf("Error opening infile\n");
		 return(1);
	 }
	 if (outfile == NULL){
		 printf("Error opening outfile\n");
		 return(1);
	 }


	if (strcmp(argv[1], "compress") == 0)
		{
			
	                compress(infile, outfile);
			fclose(infile);
			fclose(outfile);
		}
	else if(strcmp(argv[1], "decompress") == 0)
	{
	                decompress(infile, outfile);
			fclose(infile);
			fclose(outfile);
	}
	else
	{
	 printf("Usage %s [compress|decompress] infile outfile\n", argv[0]);
	 exit (-1);
	}
return 0;	
	}
