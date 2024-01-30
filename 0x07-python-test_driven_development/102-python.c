#include <Python.h>

/**
 * print_python_string - Prints Python string information
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
	}
	else if (PyBytes_Check(p))
	{
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", PyBytes_GET_SIZE(p));
		printf("  value: %s\n", PyBytes_AS_STRING(p));
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
