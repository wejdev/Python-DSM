using System.IO;
using System;

public class Program
{
    public class A
    {
        private string str;

        public A(string input)
        {
            str = input;
        }
    };

    public class B : A
    {
        public B(string input) : base(input)
        {

        }
    }

    public static void Main()
    {
        B bee = new B("bzzzz");

        //Console.WriteLine(bee.str);
    }
}

