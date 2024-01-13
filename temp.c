#include <stdio.h>


int main() 
{

      char ch, sp[100], sen[100];
      
      scanf("%c", &ch);
      scanf(" %99[^\n]", sp);
      scanf(" %99[^\n]", sen);
      
        printf("%c\n", ch);
        printf("%s\n", sp);
        printf("%s\n", sen); 
      
    return 0;
}