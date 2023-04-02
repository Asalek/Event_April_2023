#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int ac, char **av)
{
	if (ac == 2)
	{
		int sum = 0;
		char type[] = "23456789TJDKA";
		while (*av[1])
		{
			if (strchr(type, *av[1]) == NULL)
				return (printf("Bad Arguments!\n"), 1);
			if (*av[1] == 'A')
			{
				if ((sum + 11) > 21)
					sum += 1;
				else
					sum += 11;
			}
			else if (strchr("TJDK", *av[1]) != NULL)
				sum += 10;
			else
			{
				char a = *av[1];
				sum += atoi(&a);
			}
			av[1]++;
		}
		if (sum == 21)
			printf("BlackJack!\n");
		else
			printf("%d\n", sum);
	}
	return 0;
}