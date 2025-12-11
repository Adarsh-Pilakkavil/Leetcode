#include <math.h>
bool isPowerOfTwo(int n)
{
   if (n<=0)
   {
        return false;
   }
   if ((int)pow(2,30)%n==0)
   {
        return true;
   }
   else
   {
        return false;
   }
}