#include <math.h>
double power;
double fn(double x,long n)
{
    if (x==0)
    {
        return 0;
    }
    if (n==0)
    {
        return 1;
    }
    power=fn(x,n/2);
    power=power*power;
    if (n%2==1)
    {
        return power*x;
    }
    return power;    
}
double myPow(double x,long n)
{
    power=x;
    double ans=1;
    if (n>0)
    {
        ans=fn(x,n);
        return ans;
    }
    if (n<0)
    {
        ans=fn(x,-n);
        return 1/ans;
    }
    return ans;
}
