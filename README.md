# Perfov

A simple Python class for measuring performance of processes.

## Installation

```bash
pip install perfov
```

## Usage

Here's an example of how you can use Perfov in your code:

```python
from perfov import Perfov

perfov = Perfov()
perfov.start()
perfov.checkpoint(label="Rendering")
perfov.checkpoint(label="Burning")
perfov.finish()
```

The above code will output the following results:

```yaml
Performance Results:
Rendering: 0.12 seconds
Burning: 0.23 seconds
Total time: 0.35 seconds
```

## Methods

Perfov has the following methods:

- start(): Mark the start time of the performance measurement.

- checkpoint(label): Create a checkpoint for a specific process, where label is a string that describes the process.
- finish(): Print the total elapsed time for all processes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
