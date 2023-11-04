#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome - a function that checks if a list is a palindrome or not
 * @head: pointer to the adress of the head of the linked listi
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *steady, *rapid, *prev, *current, *then;
	listint_t *pal1, *pal2;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	steady = *head;
	rapid = *head;
	while (rapid->next != NULL && rapid->next->next != NULL)
	{
		steady = steady->next;
		rapid = rapid->next->next;
	}
	prev = NULL;
	current = steady->next;
	while (current != NULL)
	{
		then = current->next;
		current->next = prev;
		prev = current;
		current = then;
	}
	pal1 = *head;
	pal2 = prev;
	while (pal2 != NULL)
	{
		if (pal1->n != pal2->n)
			return (0);
		pal1 = pal1->next;
		pal2 = pal2->next;
	}
	return (1);
}





