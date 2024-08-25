using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // Example: Symmetric group S3
        var permutations = GenerateSymmetricGroup(3);

        Console.WriteLine("Permutations in S3:");
        foreach (var perm in permutations)
        {
            Console.WriteLine(string.Join(", ", perm));
        }
    }

    static List<int[]> GenerateSymmetricGroup(int n)
    {
        var elements = Enumerable.Range(1, n).ToArray();
        var permutations = new List<int[]>();
        Permute(elements, 0, permutations);
        return permutations;
    }

    static void Permute(int[] elements, int start, List<int[]> result)
    {
        if (start == elements.Length - 1)
        {
            result.Add((int[])elements.Clone());
        }
        else
        {
            for (int i = start; i < elements.Length; i++)
            {
                Swap(ref elements[start], ref elements[i]);
                Permute(elements, start + 1, result);
                Swap(ref elements[start], ref elements[i]); // backtrack
            }
        }
    }

    static void Swap(ref int a, ref int b)
    {
        int temp = a;
        a = b;
        b = temp;
    }
}