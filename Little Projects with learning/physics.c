#include<stdio.h>
int main(){

    // m1 = mass of ice
    // m2 = mass of water
    // q2 = latent heat of ice
    // q2 = latent heat of water
    // deg1  = tempreature of water
    // deg2  = tempreature of water 
    // tep = wanting tempreature

    double q2, m1, q1 , q3 ;
    int deg1, tep, f =1 ;

    printf("Enter the wanting tempreature from ice to water : \n");
    scanf("%d", &tep);

    // for ice =======================

    printf("Enter the mass of ice : \n");
    scanf("%lf", &m1);

    printf("Enter the Tempreature of ice: \n");
    scanf("%d", &deg1);

    // end ice ========================
    
   do
   {
    
        if (deg1 < 0){
            q1 = m1 * 2100 * (0 - deg1);
            q2 = m1 * 336000;
            q3 = m1 * 4200 * tep;
            f = 10;
            break;
        }
        else{
            q2 = m1 * 336000;
            q3 = m1 * 4200 * (tep - 0);
            f = 20;
            break;
        }

   } while (tep >= 1);

    if (f == 10)
    {
        printf("The value of Q1 = %.2lf\n", q1);
        printf("The value Of q2 = %.2lf\n", q2);
        printf("The value of q3 = %.2lf\n", q3);
        printf("Full q = %.2lf", q1 + q2 + q3);
    }
    else{
        printf("The value Of q2 = %.2lf\n", q2);
        printf("The value of q3 = %.2lf\n", q3);
        printf("Full q = %.2lf",  q2 + q3);

    }
    
   
   
   
    
    
    
    



    return 0;

}