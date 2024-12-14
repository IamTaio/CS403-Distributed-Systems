# Distributed Systems Projects Collection

This repository contains implementations of various distributed systems concepts and algorithms, each in its own directory. Each project focuses on different aspects of distributed computing, from concurrent data structures to blockchain implementations.

## Project Structure

### 1. Concurrent Multi-Set Implementation (`/concurrent-set`)
Implementation of a linearizable concurrent multi-set with leader election functionality.
- `ConSet.py`: Core implementation of the concurrent multi-set data structure
- `Leader.py`: Leader election algorithm implementation
- [View Detailed Documentation](concurrent-set/README.md)

**Key Features:**
- Thread-safe operations
- Queue-like implementation for efficiency
- Leader election protocol
- Coarse-grained synchronization

### 2. MapReduce Framework (`/mapreduce`)
A simplified MapReduce implementation using ZeroMQ for distributed processing.
- `MapReduce.py`: Core MapReduce framework
- `FindCitations.py`: Citation counting implementation
- `FindCyclicReferences.py`: Cyclic reference detection
- [View Detailed Documentation](mapreduce/README.md)

**Key Features:**
- Distributed processing framework
- Producer-Consumer pattern
- Citation analysis capabilities
- ZeroMQ communication

### 3. Blockchain System (`/blockchain`)
A distributed blockchain implementation using Pyro4 for remote method invocation.
- `BTCServer.py` & `ETHServer.py`: Cryptocurrency chain implementations
- `MyBlockChain.py`: Core blockchain functionality
- Client implementation files
- [View Detailed Documentation](blockchain/README.md)

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

## Project Status

- Concurrent Multi-Set: ✅ Complete
- MapReduce Framework: ✅ Complete
- Blockchain System: ✅ Complete

## Documentation

Each project directory contains:
- Detailed README with implementation details
- Usage examples
- API documentation
- Design decisions and rationale

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Additional Resources

- [Concurrent Multi-Set Report](concurrent-set/REPORT.md)
- [MapReduce Implementation Guide](mapreduce/IMPLEMENTATION.md)
- [Blockchain System Architecture](blockchain/ARCHITECTURE.md)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
