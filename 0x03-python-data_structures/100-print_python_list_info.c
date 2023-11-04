#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints the information of a python list
 * @p: a python object
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, allocated, i;
	PyObject *element;

	if (PyList_Check(p))
	{
		list = (PyListObject *)p;
		size = Py_SIZE(p);
		printf("[*] Size of the Python List = %ld\n", size);
		allocated = list->allocated;
		printf("[*] Allocated = %ld\n", allocated);

		for (i = 0; i < size; i++)
		{
			element = PyList_GET_ITEM(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		}
	}
}



