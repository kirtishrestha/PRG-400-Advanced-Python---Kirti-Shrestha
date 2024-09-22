#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

int print_message(const char* message) {
    printf("%s\n", message);
    int length = 0;
    while (message[length] != '\0') {
        length++;
    }
    return length;
}

