#include "lists.h"
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head pointer
 * @number: integer number
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new = malloc(sizeof(listint_t));
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
	*curr = *head;
	while(curr->next != NULL && curr->next->n < number)
	{
		curr = curr->next;
	}

	new->next = curr->next;
	curr-> = new;

	return(new;)
}
