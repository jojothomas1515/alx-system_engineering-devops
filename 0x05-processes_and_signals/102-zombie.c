#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>

/**
 * infinite_while - infinite loop
 * Return: 0 always
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - extry point of my program
 * Return: 0 always
 *
 */
int main(void)
{
	__pid_t process, status;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		process = fork();
		if (process == -1)
			break;
		if (process == 0)
		{
			printf("The pid of the process is = %d, the parent pid is = %d \n",
			       getpid(), getppid());
			exit(1);
		}
	}
	infinite_while();
	return (0);
}
