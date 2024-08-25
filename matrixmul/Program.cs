using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Define objects
        var A = new CategoryObject("A");
        var B = new CategoryObject("B");
        var C = new CategoryObject("C");

        // Define morphisms
        var f = new Morphism(A, B, "f");
        var g = new Morphism(B, C, "g");

        // Define composition
        var h = Morphism.Compose(f, g);

        // Print results
        Console.WriteLine($"Morphism f: {f}");
        Console.WriteLine($"Morphism g: {g}");
        Console.WriteLine($"Composition h = g ∘ f: {h}");
    }
}

class CategoryObject
{
    public string Name { get; }

    public CategoryObject(string name)
    {
        Name = name;
    }

    public override string ToString()
    {
        return Name;
    }
}

class Morphism
{
    public CategoryObject Domain { get; }
    public CategoryObject Codomain { get; }
    public string Name { get; }

    public Morphism(CategoryObject domain, CategoryObject codomain, string name)
    {
        Domain = domain;
        Codomain = codomain;
        Name = name;
    }

    public static Morphism Compose(Morphism f, Morphism g)
    {
        if (f.Codomain != g.Domain)
        {
            throw new InvalidOperationException("Cannot compose morphisms: codomain of f must match domain of g.");
        }

        return new Morphism(f.Domain, g.Codomain, $"{g.Name} ∘ {f.Name}");
    }

    public override string ToString()
    {
        return $"{Name}: {Domain} -> {Codomain}";
    }
}
