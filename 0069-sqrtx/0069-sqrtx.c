int mySqrt(int x) 
{
    long i=0;
    for (i=0;;i++)
    {
        if (i*i<=x && (i+1)*(i+1)>x)
        {
            return i;
        }
    }
}