#include <stdio.h>

// Function to multiply two numbers
int multiply(int a, int b) {
    return a * b;
}

// Function to compute Fibonacci (iterative)
int fibonacci(int n) {
    int a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
