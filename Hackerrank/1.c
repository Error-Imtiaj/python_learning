/* Your task is to take two numbers of int data type, two numbers of float data type as input and output their sum:

Declare  variables: two of type int and two of type float.
Read  lines of input from stdin (according to the sequence given in the 'Input Format' section below) and initialize your  variables.
Use the  and  operator to perform the following operations:
Print the sum and difference of two int variable on a new line.
Print the sum and difference of two float variable rounded to one decimal place on a new line. */

#include<stdio.h>
int main(int argc, char const *argv[])
{
    int a , b;
    float c , d;

    scanf("%d%d", &a, &b);
    scanf("%f%f", & c, &d );

    printf("%d %d\n", a + b, a - b);
    printf("%.1f %.1f\n", c+d, c-d);
    return 0;
}