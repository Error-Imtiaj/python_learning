""" Read two floating points' values of double precision A and B, corresponding to two student's grades. After this, calculate the student's average, considering that grade A has weight 3.5 and B has weight 7.5. Each grade can be from zero to ten, always with one digit after the decimal point. Don’t forget to print the end of line after the result, otherwise you will receive “Presentation Error”. Don’t forget the space before and after the equal sign. """

A = float(input())
B = float(input())
weight_a = 3.5
weight_b = 7.5

MEDIA = (A * weight_a + B * weight_b)/ (weight_b + weight_a)

print("MEDIA = {:.5f}".format(MEDIA))