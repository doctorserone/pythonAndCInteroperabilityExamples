#include <Python.h>

// References:
// https://realpython.com/build-python-c-extension-module/

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

static PyObject *fibonacciExtension(PyObject *self, PyObject *args) {
    int count = 0;

    // Parse arguments
    // https://docs.python.org/3/c-api/arg.html
    if(!PyArg_ParseTuple(args, "i", &count)) {
        return NULL;
    }

    int result = fibonacci(count);

    // All integers are implemented as “long” integer objects of arbitrary size
    // https://docs.python.org/3/c-api/long.html
    return PyLong_FromLong(result);
}

// In order to call the methods defined in your module, you’ll need to tell the Python interpreter about them first. 
// To do this, you can use PyMethodDef. This is a structure with 4 members representing a single method in your module.
// Ideally, there will be more than one method in your Python C extension module that you want to be callable from 
// the Python interpreter. This is why you need to define an array of PyMethodDef structs:

static PyMethodDef fibonacciMethods[] = {
    {"fibonacciExtension", fibonacciExtension, METH_VARARGS, "Python extension for fibonacci"},
    {NULL, NULL, 0, NULL}
};

// Just as PyMethodDef holds information about the methods in your Python C extension module, the PyModuleDef struct 
// holds information about your module itself. It is not an array of structures, but rather a single structure that’s 
// used for module definition:

static struct PyModuleDef fibonacciExtensionModule = {
    PyModuleDef_HEAD_INIT,
    "fibonacciExtension",
    "Python extension for fibonacci",
    -1,
    fibonacciMethods
};

// Now that you’ve defined your Python C extension module and method structures, it’s time to put them to use. 
// When a Python program imports your module for the first time, it will call PyInit_*():

PyMODINIT_FUNC PyInit_fibonacciExtension(void) {
    return PyModule_Create(&fibonacciExtensionModule);
}