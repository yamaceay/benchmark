"""Example usage of the benchmark module."""

from benchmark.squad import SquadBenchmark
from benchmark.tab import TabBenchmark


class DummyModel:
    """Dummy model for demonstration purposes."""
    
    def predict(self, *args, **kwargs):
        """Return a dummy prediction."""
        return "dummy answer"


def main():
    """Demonstrate usage of different benchmarks."""
    print("=" * 60)
    print("Benchmark Module - Example Usage")
    print("=" * 60)
    
    # Example 1: SQuAD Benchmark
    print("\n1. SQuAD Benchmark")
    print("-" * 60)
    squad = SquadBenchmark()
    print(f"Initialized: {squad.name}")
    squad.load_data()  # Would load actual data in production
    print(f"Loaded {len(squad.data)} samples")
    
    # Example 2: TAB Benchmark
    print("\n2. TAB Benchmark")
    print("-" * 60)
    tab = TabBenchmark()
    print(f"Initialized: {tab.name}")
    tab.load_data()  # Would load actual data in production
    print(f"Loaded {len(tab.data)} samples")
    
    # Example 3: Using from another module
    print("\n3. Integration Example")
    print("-" * 60)
    print("In another module, you can import and use like:")
    print("\n  from benchmark.squad import SquadBenchmark")
    print("  from benchmark.tab import TabBenchmark")
    print("\n  # Initialize and run benchmark")
    print("  benchmark = SquadBenchmark()")
    print("  benchmark.load_data('path/to/data.json')")
    print("  results = benchmark.run(my_model)")
    print("  print(results)")
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
