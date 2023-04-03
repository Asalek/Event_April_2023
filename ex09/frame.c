#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int biggest(char *str)
{
	int len = 7;
	char *s = strtok(str, " ");
	len = strlen(s);
	while (s != NULL)
	{
		s = strtok(NULL, " ");
		if (s && len < strlen(s))
			len = strlen(s);
	}
	return len;
}

int main(int ac, char *av[])
{
	int space = 0;
	if (ac == 2)
	{
		int spaces = biggest(strdup(av[1]));
		char *a = malloc(spaces + 4);
		a = memset(a, '*', spaces+ 4);
		char *b = malloc(spaces + 4);
		b = memset(b, ' ', spaces + 4);

		char *str = strtok(av[1], " ");

		printf("%.*s\n", spaces + 4, a);
		while (str != NULL)
		{
			printf("* %s %.*s*\n", str, (int)(spaces - strlen(str)), b);
			str = strtok(NULL, " ");
		}
		printf("%.*s\n", spaces + 4, a);
	}
	return 0;
}