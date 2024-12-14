# MapReduce Framework using ZeroMQ

## 1. Project Overview

This project implements a simplified MapReduce framework using ZeroMQ sockets for distributed processing. The framework is designed to analyze academic paper citation networks with the following features:

- Distributed processing using Producer-Consumer pattern
- Parallel execution using multiple worker processes
- ZeroMQ socket communication for data transfer
- Support for citation counting and cyclic reference detection
- Configurable number of worker processes (up to 10)

### Key Technologies
- Python 3.x
- ZeroMQ (pyzmq)
- Multiprocessing
- JSON for data serialization

### Core Components
- Abstract MapReduce base class
- FindCitations implementation for citation counting
- FindCyclicReferences implementation for detecting mutual citations
- Command-line interface for execution control

## 2. Problem Statement

This framework addresses two specific problems in citation network analysis:

### Citation Counting
- **Input**: Tab-separated pairs of paper IDs (citingPaper citedPaper)
- **Output**: Dictionary of paper IDs and their citation counts
- **Example**:
  ```
  Input:
  1   2
  3   2
  4   2
  
  Output:
  {'2': 3, '1': 0, '3': 0, '4': 0}
  ```

### Cyclic Reference Detection
- **Input**: Same format as citation counting
- **Output**: Dictionary of paper ID pairs that cite each other
- **Example**:
  ```
  Input:
  1   2
  2   1
  3   4
  
  Output:
  {'(1, 2)': 1}
  ```

## 3. Implementation Details

### Main Components

#### MapReduce Base Class
- Abstract base class defining the MapReduce framework
- Handles process management and data distribution
- Implements Producer-Consumer pattern using ZeroMQ

#### Key Methods
- `start(filename)`: Entry point that initiates processing
- `__producer__`: Distributes input data to workers
- `__consumer__`: Processes data chunks in parallel
- `__result_collector__`: Aggregates results from workers
- Abstract `Map` and `Reduce` methods for subclass implementation

### Data Structures
- Input data: List of integer pairs
- Intermediate results: Dictionaries
- Final output: Dictionary stored in results.txt

## 4. Usage Instructions

### Requirements
- Python 3.x
- pyzmq package
- multiprocessing module

### Installation
```bash
pip install pyzmq
```

### Running the Program
```bash
python main.py <OPERATION> <NUM_WORKERS> <INPUT_FILE>
```

### Parameters
- `OPERATION`: Either `COUNT` (for citations) or `CYCLE` (for cyclic references)
- `NUM_WORKERS`: Number of parallel workers (1-10)
- `INPUT_FILE`: Path to input data file

### Example Commands
```bash
python main.py COUNT 4 test01.txt
python main.py CYCLE 3 test02.txt
```

## 5. Error Handling

The program handles several types of errors:

- Invalid number of command-line arguments
- Unsupported operation types (only COUNT and CYCLE allowed)
- Non-numeric worker count
- Worker count exceeding maximum (10)
- Missing input file
- Malformed input data (handled by skipping)

## 6. Example Session

### Citation Counting Example
```bash
$ python main.py COUNT 4 test01.txt
Find Citations called
Consumer PID: 12345
ResultCollector PID: 12346
```
Output in results.txt:
```python
{'1': 0, '2': 3, '3': 1, '4': 2}
```

### Cyclic References Example
```bash
$ python main.py CYCLE 3 test02.txt
Find Cyclic References called
Consumer PID: 12347
ResultCollector PID: 12348
```
Output in results.txt:
```python
{'(1, 2)': 1, '(3, 4)': 1}
```

Note: Results are written to results.txt in the working directory.
