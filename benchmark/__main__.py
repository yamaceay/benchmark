"""Main entry point for running benchmarks directly."""

import sys
from typing import List


def main(args: List[str] = None) -> None:
    """Main function to run benchmarks from command line.
    
    Args:
        args: Command line arguments
    """
    if args is None:
        args = sys.argv[1:]
    
    if not args or args[0] in ["-h", "--help"]:
        print("Benchmark Module - LLM Evaluation Framework")
        print("\nUsage:")
        print("  python -m benchmark <benchmark_name> [options]")
        print("\nAvailable benchmarks:")
        print("  squad  - SQuAD (Stanford Question Answering Dataset)")
        print("  tab    - TAB (Tabular dataset)")
        print("\nExamples:")
        print("  python -m benchmark squad")
        print("  python -m benchmark tab")
        return
    
    benchmark_name = args[0].lower()
    
    if benchmark_name == "squad":
        from benchmark.squad import SquadBenchmark
        bench = SquadBenchmark()
        print(f"\n{bench.name} Benchmark initialized")
        print("Use the load_data() method to load your dataset")
        print("Use the run(model) method to evaluate your model")
        
    elif benchmark_name == "tab":
        from benchmark.tab import TabBenchmark
        bench = TabBenchmark()
        print(f"\n{bench.name} Benchmark initialized")
        print("Use the load_data() method to load your dataset")
        print("Use the run(model) method to evaluate your model")
        
    else:
        print(f"Error: Unknown benchmark '{benchmark_name}'")
        print("Available benchmarks: squad, tab")
        sys.exit(1)


if __name__ == "__main__":
    main()
