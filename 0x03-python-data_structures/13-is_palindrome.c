#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (0);
	return (palind(head, *head));
}

/**
 * palind -if is palindrome with recursion
 * @start: ptr to ptr
 * @end: pointer
 * Return: 1 palind,or 0 if not palind
 */
int palind(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (0);
	if (palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (0);
	}
	return (0);
}
