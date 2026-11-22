using System;

class Program
{
    static bool IsPrime(int n)
    {
        if (n <= 1)
            return false;

        for (int i = 2; i < n; i++)
        {
            if (n % i == 0)
            {
                return false;
            }
        }

        return true;
    }
    
    static int CountPrimes(int a, int b)
    {
        int i=a;
        int counter = 0;
        while(i<=b)
        {
            if(IsPrime(i)==true)
            {
                counter++;
            }
            i++;
        }
        return counter;
    }

    static void Main()
    {
        for (int i = 1; i<=200; i++)
        {
            if(IsPrime(i) == true)
            {
                Console.Write(i+", ");
            }
        }
    Console.WriteLine("\n------------------");
    int a=1;
    int b=100;
    Console.WriteLine("Between {0} and {1} we have {2} prime numbers.", a,b,CountPrimes(a,b));
    a=101;
    b=200;
    Console.WriteLine("Between {0} and {1} we have {2} prime numbers.", a,b,CountPrimes(a,b));
    a=1;
    b=100000;
    Console.WriteLine("Between {0} and {1} we have {2} prime numbers.", a,b,CountPrimes(a,b));
    }
}