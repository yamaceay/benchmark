# benchmark
Benchmarking for LLMs

A modular framework for benchmarking Large Language Models across different datasets. Each benchmark is organized in its own folder and can be executed directly from another module.

## Features

- **Modular Structure**: Each benchmark dataset (SQuAD, TAB, etc.) is in a separate folder
- **Easy Integration**: Can be imported and used as a submodule in other projects
- **Extensible**: Base class architecture makes it easy to add new benchmarks
- **Direct Execution**: Can be run directly using `python -m benchmark`

## Installation

```bash
# Install from source
pip install -e .

# Or install from the repository
pip install git+https://github.com/yamaceay/benchmark.git
```

## Project Structure

```
benchmark/
├── benchmark/
│   ├── __init__.py          # Main package initialization
│   ├── __main__.py          # Direct execution entry point
│   ├── base/                # Base classes and utilities
│   │   ├── __init__.py
│   │   └── benchmark_base.py
│   ├── squad/               # SQuAD benchmark
│   │   ├── __init__.py
│   │   └── squad_benchmark.py
│   └── tab/                 # TAB benchmark
│       ├── __init__.py
│       └── tab_benchmark.py
├── pyproject.toml           # Package configuration
├── README.md
└── LICENSE
```

## Usage

### As a Module (Recommended)

```python
# Import and use SQuAD benchmark
from benchmark.squad import SquadBenchmark

squad = SquadBenchmark()
squad.load_data("path/to/squad/data.json")
results = squad.run(your_model)
print(results)
```

```python
# Import and use TAB benchmark
from benchmark.tab import TabBenchmark

tab = TabBenchmark()
tab.load_data("path/to/tab/data.csv")
results = tab.run(your_model)
print(results)
```

### Direct Execution

```bash
# Run SQuAD benchmark
python -m benchmark squad

# Run TAB benchmark
python -m benchmark tab

# Show help
python -m benchmark --help
```

### Creating a Custom Benchmark

```python
from benchmark.base import BenchmarkBase
from typing import Any, Dict, List

class MyCustomBenchmark(BenchmarkBase):
    def __init__(self):
        super().__init__("MyCustom")
        self.data = []
    
    def load_data(self, data_path: str = None) -> None:
        # Implement your data loading logic
        pass
    
    def run(self, model: Any) -> Dict[str, Any]:
        # Implement your benchmark logic
        predictions = []
        ground_truth = []
        # ... get predictions from model ...
        return self.evaluate(predictions, ground_truth)
    
    def evaluate(self, predictions: List[Any], ground_truth: List[Any]) -> Dict[str, float]:
        # Implement your evaluation metrics
        return {"accuracy": 0.0}
```

## Available Benchmarks

### SQuAD (Stanford Question Answering Dataset)
Located in `benchmark/squad/`

A reading comprehension dataset consisting of questions posed on Wikipedia articles.

**Metrics**: F1 Score, Exact Match

### TAB (Tabular Dataset)
Located in `benchmark/tab/`

Benchmark for evaluating models on structured/tabular data tasks.

**Metrics**: Accuracy, Precision, Recall

## Adding New Benchmarks

1. Create a new folder under `benchmark/` (e.g., `benchmark/new_dataset/`)
2. Add `__init__.py` and implement your benchmark class extending `BenchmarkBase`
3. Implement the required methods: `load_data()`, `run()`, and `evaluate()`
4. Update the `__main__.py` to include your new benchmark

## Development

```bash
# Clone the repository
git clone https://github.com/yamaceay/benchmark.git
cd benchmark

# Install in development mode
pip install -e .

# Run tests (if available)
python -m pytest
```

## License

MIT License - see [LICENSE](LICENSE) file for details

## Author

Yamac Eren Ay
