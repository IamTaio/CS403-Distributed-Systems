# Distributed Systems Projects Collection

This repository contains implementations of various distributed systems concepts and algorithms, each in its own directory. Each project focuses on different aspects of distributed computing, from concurrent data structures to blockchain implementations.

## Project Structure

### 1. Concurrent Multi-Set Implementation (`/Linearizable-Concurrent-Multi-set`)

Implementation of a linearizable concurrent multi-set with leader election functionality.

- `ConSet.py`: Core implementation of the concurrent multi-set data structure
- `Leader.py`: Leader election algorithm implementation
- [View Detailed Documentation](Linearizable-Concurrent-Multi-set/README.md)

**Key Features:**

- Thread-safe operations
- Queue-like implementation for efficiency
- Leader election protocol
- Coarse-grained synchronization

### 2. MapReduce Framework (`/MapReduce`)

A simplified MapReduce implementation using ZeroMQ for distributed processing.

- `MapReduce.py`: Core MapReduce framework
- `FindCitations.py`: Citation counting implementation
- `FindCyclicReferences.py`: Cyclic reference detection
- [View Detailed Documentation](MapReduce/README.md)

**Key Features:**

- Distributed processing framework
- Producer-Consumer pattern
- Citation analysis capabilities
- ZeroMQ communication

### 3. Blockchain System (`/Blockchain-Implementation-using-Pyro4`)

A distributed blockchain implementation using Pyro4 for remote method invocation.

- `BTCServer.py` & `ETHServer.py`: Cryptocurrency chain implementations
- `MyBlockChain.py`: Core blockchain functionality
- Client implementation files
- [View Detailed Documentation](Blockchain-Implementation-using-Pyro4/README.md)

**Key Features:**

- Multiple cryptocurrency chain support
- Inter-chain transactions
- Thread-safe operations
- Remote method invocation

## Getting Started

Each project has its own setup requirements and dependencies. Navigate to the specific project directory and refer to its README for detailed instructions.

### General Prerequisites

- Python 3.x
- pip (Python package manager)

### Common Dependencies

```bash
# For MapReduce project
pip install pyzmq

# For Blockchain project
pip install Pyro4

# For testing
pip install pytest
```

## Running the Projects

### Concurrent Multi-Set

```bash
cd concurrent-set
python Leader.py
```

### MapReduce

```bash
cd mapreduce
python main.py COUNT 4 test01.txt
# or
python main.py CYCLE 3 test02.txt
```

### Blockchain

```bash
# Terminal 1
python -m Pyro4.naming

# Terminal 2
cd blockchain
python BTCServer.py

# Terminal 3
python ETHServer.py

# Terminal 4
python firstClient.py
```
