#include <stdio.h>
#include <gsl/gsl_linalg.h>
int n=3;
int main()
{
    double M[] = {1, 0.67, 0.33, 0.45, 1, 0.55, 0.67, 0.33, 1};
    int i,j,k;
    int condition = 0;

    gsl_matrix *m = gsl_matrix_alloc( n, n);
    gsl_matrix *A = gsl_matrix_alloc(n, n);

    printf("A = \n");
    for(i = 0;i<n;i=i+1)
    {
      for(j=0;j<n;j=j+1)
      {
        gsl_matrix_set(m,i,j,M[i*n+j]);
        gsl_matrix_set(A,i,j,M[i*n+j]);
        printf("%0.2f\t\t",M[i*n+j]);
      }
      printf("\n");
    }
    printf("\n");

    int sign;
    gsl_permutation *p = gsl_permutation_alloc(n);


    gsl_linalg_LU_decomp(m, p, &sign);

    gsl_matrix *U = gsl_matrix_alloc(n,n);
    gsl_matrix *L = gsl_matrix_alloc(n,n);
printf("L = \n");

    for(i=0;i<n;i=i+1)
    {
      for(j=0;j<n;j=j+1)
      {
        if(j>i)
          {printf("0.00\t\t");gsl_matrix_set(L,i,j,0);}
        else
        {
          if(j == i)
            {printf("1.00\t\t");gsl_matrix_set(L,i,j,1);}
          else
            {printf("%0.2f\t\t",gsl_matrix_get(m,i,j));gsl_matrix_set(L,i,j,gsl_matrix_get(m,i,j));}
        }
      }
      printf("\n");
    }
    printf("\n");
    
    printf("U = \n");

    for (i=0;i<n;i=i+1)
    {
      for (j = 0;j<n;j=j+1)
      {
        if(j<i)
          {printf("0.00\t\t");gsl_matrix_set(U,i,j,0);}
        else
        {printf("%0.2f\t\t",gsl_matrix_get(m,i,j));gsl_matrix_set(U,i,j,gsl_matrix_get(m,i,j));}
      }
      printf("\n");
    }
    printf("\n");


    


    gsl_matrix *P = gsl_matrix_alloc(3,3);
    gsl_matrix *Identity = gsl_matrix_alloc(3,3);
    gsl_matrix_set_identity(Identity);

    printf("P = \n");

    for(i=0;i<n;i=i+1)
    {
      for(j=0;j<n;j=j+1)
      {
        gsl_matrix_set(P,i,j,gsl_matrix_get(Identity,i,gsl_permutation_get(p,j)));
        printf("%0.2f\t\t",gsl_matrix_get(P,i,j));
      }
      printf("\n");
    }


    double a = 0;
    double b = 0;

    for(i = 0;i<n;i=i+1)
    {
      for(j=0;j<n;j=j+1)
      {
        for(k=0;k<n;k=k+1)
        {
          a = a + gsl_matrix_get(P,i,k)*gsl_matrix_get(A,k,j);
          b = b + gsl_matrix_get(L,i,k)*gsl_matrix_get(U,k,j);
        }
        if(a != b)
          condition = 1;
        a = 0;
        b = 0;
      }
    }

    if(condition == 1)
      printf("PA is not equal to LU\n");
    else
      printf("PA and LU equalize \n");


    gsl_permutation_free(p);
    gsl_matrix_free(m);
    gsl_matrix_free(U);
    gsl_matrix_free(L);
    gsl_matrix_free(P);
    gsl_matrix_free(Identity);
    return 0;
}
