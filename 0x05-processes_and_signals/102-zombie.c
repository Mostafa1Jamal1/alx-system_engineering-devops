#include <stdio.h>
#include <unistd.h>
/**
 * main - creates 5 zombie processes.
 * Return: 0 (success) -Which is never as infinite loop-
 */

int infinite_while(void);

int main(void)
{
	int i;
	pid_t child = 1;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		/* print in the parent */
		if (child > 0)
			printf("Zombie process created, PID: %d\n", child);
		/* Return from child */
		if (child == 0)
			return (0);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - keeps the program running
 * Return: 0 (Success) -Which is never as infinite loop-
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
