""" Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place. """

a = float(input())
b = float(input())
c = float(input())

weight_a = 2.0
weight_b = 3.0
weight_c = 5.0

MEDIA = (a * weight_a + b * weight_b + c * weight_c) / (weight_a + weight_b + weight_c)
print("MEDIA = {:.1f}".format(MEDIA))