#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
  if (head == NULL || *head == NULL)
  {
    return (1);
  }
  return (palind(head, *head));
}

/**
 * palind - Checks if the remaining list is a palindrome.
 * @head: Pointer to the head of the remaining list.
 * @end: Tail of the remaining list.
 *
 * Return: 1 if palindrome, 0 if not palindrome.
 */
int palind(listint_t **head, listint_t *end)
{
  if (end == NULL)
  {
    return (1);
  }

  if (palind(head, end->next) && (*head)->n == end->n) {
    *head = (*head)->next;
    return (1);
  }

  return (0);
}
