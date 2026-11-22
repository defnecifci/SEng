
using System;
class Factorial {
  static void Main() {
    int n = 6;
    int result = 1;
    
    for (int i=1; i<=n; i++)
    {
        result = result*i;
    }
    
    Console.WriteLine(n+"! = "+result);
  }
}