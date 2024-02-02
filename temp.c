#include<stdio.h>
int main(){

  float angle1, angle2, angle3;
  scanf("%f%f%f", &angle1, &angle2, &angle3);

  if (angle1 + angle2 + angle3 == 180)
  {
    printf("The Triangle will be possible\n");
  }
  else{
    printf("The triangle will not possible\n");
  }
  
  return 0;
}