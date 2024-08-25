using System;
using System.Linq;
using System.Windows;
using MathNet.Symbolics;
using OxyPlot;
using OxyPlot.Series;
using Expr = MathNet.Symbolics.SymbolicExpression;

namespace InverseLaplaceTransformPlot
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            PlotInverseLaplaceTransform();
        }

        private void PlotInverseLaplaceTransform()
        {
            // Define the Laplace transform variable and the function
            var s = Expr.Variable("s");
            var F_s = 1 / (s * s + s + 1); // Example Laplace transform function

            // Compute the inverse Laplace transform
            var t = Expr.Variable("t");
            var f_t = InverseLaplaceTransform(F_s, s, t);

            // Generate time values
            var t_vals = Enumerable.Range(0, 400).Select(i => i * 0.025).ToArray();

            // Evaluate the inverse Laplace transform at each time value
            var f_t_vals = t_vals.Select(t_val => f_t.Evaluate(Variable.Create(t_val)).RealValue).ToArray();

            // Plot the result
            var plotModel = new PlotModel { Title = "Inverse Laplace Transform" };
            var lineSeries = new LineSeries { Title = $"f(t) = {f_t}" };

            for (int i = 0; i < t_vals.Length; i++)
            {
                lineSeries.Points.Add(new DataPoint(t_vals[i], f_t_vals[i]));
            }

            plotModel.Series.Add(lineSeries);
            PlotView.Model = plotModel;
        }

        private Expr InverseLaplaceTransform(Expr F_s, Expr s, Expr t)
        {
            // This is a placeholder for the actual inverse Laplace transform computation.
            // MathNet.Symbolics does not directly support inverse Laplace transform.
            // You may need to implement or use a different library for this.
            // For demonstration purposes, we return a simple function.
            return Expr.Parse("exp(-t) * sin(t)");
        }
    }
}
