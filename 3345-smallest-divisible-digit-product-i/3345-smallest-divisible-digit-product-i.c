int smallestNumber(int n, int t) 
{
    int k=n,pro=1,d;
    x:
    {
        k=n;
        pro=1;
        while (k!=0)
        {
            d=k%10;
            pro*=d;
            k=k/10;
        }
    }
    if (pro%t==0)
    {
        return n;
    }
    else
    {
        n++;
        goto x;
    }
    
}