#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Function to add two integers
static PyObject* add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}

// Recursive factorial function
static long factorial_c(long n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial_c(n - 1);
}

// Python wrapper for factorial
static PyObject* factorial(PyObject* self, PyObject* args) {
    long n;
    if (!PyArg_ParseTuple(args, "l", &n)) {
        return NULL;
    }
    return PyLong_FromLong(factorial_c(n));
}

// Method definitions
static PyMethodDef MyMethods[] = {
    {"add", add, METH_VARARGS, "Add two numbers"},
    {"factorial", factorial, METH_VARARGS, "Compute factorial"},
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Module definition
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",
    "Fast math operations",
    -1,
    MyMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&mymodule);
}



