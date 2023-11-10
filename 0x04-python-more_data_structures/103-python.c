#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	printf("\n");
}

/**
 * print_list - Print information about Python list
 * @p: PyObject pointer to a Python list object
 */
void print_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyLong_Check(item))
			printf("int\n");
		else if (PyFloat_Check(item))
			printf("float\n");
		else if (PyTuple_Check(item))
			printf("tuple\n");
		else if (PyList_Check(item))
			printf("list\n");
		else if (PyUnicode_Check(item))
			printf("str\n");
		else
			printf("[ERROR] Unknown Element Type\n");
	}
}
