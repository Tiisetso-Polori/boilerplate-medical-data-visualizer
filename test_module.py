import unittest
import medical_data_visualizer

class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.df = medical_data_visualizer.load_data()
        self.df = medical_data_visualizer.preprocess_data(self.df)
        self.fig = medical_data_visualizer.draw_cat_plot(self.df)

    def test_cat_plot(self):
        self.assertIsNotNone(self.fig, "Cat plot figure is None")

class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.df = medical_data_visualizer.load_data()
        self.df = medical_data_visualizer.preprocess_data(self.df)
        self.fig = medical_data_visualizer.draw_heat_map(self.df)

    def test_heat_map(self):
        self.assertIsNotNone(self.fig, "Heatmap figure is None")

if __name__ == "__main__":
    unittest.main()
