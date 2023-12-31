#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head pointer
 * @number: integer number
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *curr = *head;
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if(*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while(curr->next != NULL && curr->next->n < number)
	{
		curr = curr->next;
	}

	new->next = curr->next;
	curr->next = new;

	return(new);
}
