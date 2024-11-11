Imports System
Imports System.Data

Module Program

    Public num1 As Integer
    Public num2 As Integer
    Public answer As Integer


    Sub Main(args As String())

        Console.WriteLine("Hello World!")

        Console.Write("Please enter your name: ")

        Dim name = Console.ReadLine()

        Dim currentDate = DateTime.Now

        Console.WriteLine($"Hello, {name}, on {currentDate:d} at {currentDate:t}")

        Console.Write("Press any key to continue... ")

        Console.ReadKey(True)


        Console.WriteLine("Second Part!")

        Console.Write("Type a number and press Enter: ")

        num1 = Console.ReadLine()

        Console.Write("Type aother number to add to it and press Enter: ")

        num2 = Console.ReadLine()

        answer = num1 + num2

        Console.WriteLine("The answer is " & answer)

        Console.Write("Press any key to continue... ")

        Console.ReadKey(True)


    End Sub
End Module
