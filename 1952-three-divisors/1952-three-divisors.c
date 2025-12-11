bool isThree(int n) 
{
    int i=1,test=0;
    for (i=1;i<=n;i++)
    {
        if (n%i==0)
        {
            test++;
        }
    }
    if (test==3)
    {
        return true;
    }
    else
    {
        return false;
    }
}