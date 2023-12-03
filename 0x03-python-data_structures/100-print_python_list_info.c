#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *element;
	const char *elementType;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		elementType = Py_TYPE(element)->tp_name;

		printf("Element %d: %s\n", i, elementType);
	}
}
