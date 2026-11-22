using System;
class Triangle {
  static void Main() {
    Random random = new Random();
    double a = random.Next(1,10);
    double b = random.Next(1,10);
    double c = random.Next(1,10);
    
    Console.WriteLine("{0} {1} {2}", a,b,c);
    
    if ((b+c>a) && (a+c>b) && (b+a>c))  //the condition for a triangle
    {
        Console.WriteLine("You can build a triangle");
    }
    
    else
    {
        Console.WriteLine("You can NOT build a triangle");
    }
    
  }
}