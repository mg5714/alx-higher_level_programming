#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - info for Python list
 * @p: object
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *element;
	i = 0;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	while (i < size)
	{
		element = PyList_GET_ITEM(p, i);
		

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		i++;
	}
}
