

int fib(int n)
{
    int t0=0,t1=1,tn,i;
    if (n==0)
    {
        return t0;
    }
    if (n>1)
    {
        for (i=0;i<=n-2;i++)
        {
            tn=t1;
            t1=t0+t1; 
            t0=tn;
        }
    }
    
    return t1;
}