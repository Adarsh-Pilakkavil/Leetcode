int sumOfTheDigitsOfHarshadNumber(int x)
{
    int k=x,sum=0;
    while (k!=0)
    {
        sum+=k%10;
        k=k/10;
    }
    if (x%sum==0)
    {
        return sum;
    }
    else
    {
        return -1;
    }
}