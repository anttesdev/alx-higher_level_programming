#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to the Python bytes object to be analyzed.
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *raw_str;
	Py_ssize_t size;
	int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	printf("  size: %zd\n", size);
	raw_str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", raw_str);
	printf("  first 10 bytes: ");
	for (i = 0; i < 10 && i < size; ++i)
		printf("%02x ", (unsigned char)raw_str[i]);
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: PyObject pointer representing the Python float object
 * Return: nothing
 */

void print_python_float(PyObject *p)
{
	double result;

	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("[.] float object info\n");
	result = ((PyFloatObject *)(p))->ob_fval;
	printf("  value: %f\n", result);
}

/**
 * print_python_list - Prints information about a Python list object
 * @p: PyObject pointer representing the Python list object
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *total;
	PyObject *pyt;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Python list info\n");
	size = ((PyVarObject *)(p))->ob_size;
	total = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", total->allocated);

	for (i = 0; i < size; i++)
	{
		pyt = total->ob_item[i];
		printf("Element %ld: %s\n", i, ((pyt)->ob_type)->tp_name);

		if (PyBytes_Check(pyt))
			print_python_bytes(pyt);
		if (PyFloat_Check(pyt))
			print_python_float(pyt);
	}
}


