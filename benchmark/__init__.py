"""
Benchmark module for LLM evaluation.

This module provides a framework for benchmarking LLMs across different datasets.
Each dataset has its own submodule with specific implementations.
"""

from benchmark.base.benchmark_base import BenchmarkBase

__version__ = "0.1.0"
__all__ = ["BenchmarkBase"]
