#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to a pointer to the head of the list.
 * @number: The integer to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *present, *preceding;

	present = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (number <= present->n)
	{
		new_node->next = present;
		*head = new_node;
		return (new_node);
	}
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (present != NULL)
	{
		if (number <= present->n)
		{
			new_node->next = present;
			preceding->next = new_node;
			return (new_node);
		}
		preceding = present;
		present = present->next;
	}
	preceding->next = new_node;
	return (new_node);
}

