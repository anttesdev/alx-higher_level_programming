#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *steady, *rapid;

	if (list == NULL || list->next == NULL)
		return (0);
	steady = list;
	rapid = list->next;

	while (steady != NULL && rapid != NULL && rapid->next != NULL)
	{
		if (steady == rapid)
			return (1);
		steady = steady->next;
		rapid = rapid->next->next;
	}
	return (0);
}

