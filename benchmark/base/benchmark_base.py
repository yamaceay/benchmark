"""Base class for all benchmarks."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BenchmarkBase(ABC):
    """Abstract base class for all benchmarks.
    
    This class defines the interface that all benchmark implementations must follow.
    Each benchmark should implement the abstract methods to provide dataset-specific
    functionality.
    """
    
    def __init__(self, name: str):
        """Initialize the benchmark.
        
        Args:
            name: Name of the benchmark
        """
        self.name = name
        self.results: List[Dict[str, Any]] = []
    
    @abstractmethod
    def load_data(self) -> None:
        """Load the benchmark dataset.
        
        This method should load the dataset and prepare it for evaluation.
        """
        pass
    
    @abstractmethod
    def run(self, model: Any) -> Dict[str, Any]:
        """Run the benchmark on a given model.
        
        Args:
            model: The model to evaluate
            
        Returns:
            Dictionary containing benchmark results
        """
        pass
    
    @abstractmethod
    def evaluate(self, predictions: List[Any], ground_truth: List[Any]) -> Dict[str, float]:
        """Evaluate predictions against ground truth.
        
        Args:
            predictions: List of model predictions
            ground_truth: List of ground truth values
            
        Returns:
            Dictionary of evaluation metrics
        """
        pass
    
    def get_results(self) -> List[Dict[str, Any]]:
        """Get all benchmark results.
        
        Returns:
            List of result dictionaries
        """
        return self.results
    
    def clear_results(self) -> None:
        """Clear all stored results."""
        self.results = []
