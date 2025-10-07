"""Tests for benchmark implementations."""

import unittest
from benchmark.squad import SquadBenchmark
from benchmark.tab import TabBenchmark
from benchmark.base import BenchmarkBase


class TestBenchmarkBase(unittest.TestCase):
    """Test base benchmark functionality."""
    
    def test_squad_initialization(self):
        """Test SQuAD benchmark initialization."""
        squad = SquadBenchmark()
        self.assertEqual(squad.name, "SQuAD")
        self.assertIsInstance(squad, BenchmarkBase)
        self.assertEqual(len(squad.results), 0)
        self.assertEqual(len(squad.data), 0)
    
    def test_tab_initialization(self):
        """Test TAB benchmark initialization."""
        tab = TabBenchmark()
        self.assertEqual(tab.name, "TAB")
        self.assertIsInstance(tab, BenchmarkBase)
        self.assertEqual(len(tab.results), 0)
        self.assertEqual(len(tab.data), 0)
    
    def test_squad_evaluate_empty(self):
        """Test SQuAD evaluation with empty data."""
        squad = SquadBenchmark()
        results = squad.evaluate([], [])
        self.assertIn("f1", results)
        self.assertIn("exact_match", results)
        self.assertEqual(results["f1"], 0.0)
        self.assertEqual(results["exact_match"], 0.0)
    
    def test_tab_evaluate_empty(self):
        """Test TAB evaluation with empty data."""
        tab = TabBenchmark()
        results = tab.evaluate([], [])
        self.assertIn("accuracy", results)
        self.assertEqual(results["accuracy"], 0.0)
    
    def test_clear_results(self):
        """Test clearing results."""
        squad = SquadBenchmark()
        squad.results.append({"test": "result"})
        self.assertEqual(len(squad.results), 1)
        squad.clear_results()
        self.assertEqual(len(squad.results), 0)
    
    def test_get_results(self):
        """Test getting results."""
        tab = TabBenchmark()
        test_result = {"accuracy": 0.95}
        tab.results.append(test_result)
        results = tab.get_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], test_result)


class TestImports(unittest.TestCase):
    """Test that imports work correctly."""
    
    def test_import_squad(self):
        """Test importing SQuAD benchmark."""
        from benchmark.squad import SquadBenchmark
        self.assertIsNotNone(SquadBenchmark)
    
    def test_import_tab(self):
        """Test importing TAB benchmark."""
        from benchmark.tab import TabBenchmark
        self.assertIsNotNone(TabBenchmark)
    
    def test_import_base(self):
        """Test importing base class."""
        from benchmark.base import BenchmarkBase
        self.assertIsNotNone(BenchmarkBase)
    
    def test_import_from_main_package(self):
        """Test importing from main package."""
        from benchmark import BenchmarkBase
        self.assertIsNotNone(BenchmarkBase)


if __name__ == "__main__":
    unittest.main()
