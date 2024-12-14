# Distributed Blockchain System

## 1. Project Overview

This project implements a distributed blockchain system using Pyro4 for remote object communication. The system simulates multiple cryptocurrency chains (BTC and ETH) with the following features:

- Account creation and management
- Intra-chain transfers
- Inter-chain exchanges
- Concurrent transaction handling
- Thread-safe operations
- Remote method invocation

### Key Technologies
- Python 3.x
- Pyro4 (Python Remote Objects)
- Threading for concurrency control
- Object-oriented design with inheritance

### Core Components
- Blockchain server implementations (BTC and ETH)
- Block structure for transactions
- Client interface for testing
- Thread-safe transaction processing

## 2. Problem Statement

This system solves the challenge of implementing a distributed ledger with the following requirements:

### Transaction Management
- **Input**: Account creation requests, transfer requests, exchange requests
- **Output**: Transaction confirmation and updated chain state
- **Example Operations**:
  ```python
  # Account Creation
  acc1 = BTC.createAccount(100)  # Returns account number
  
  # Transfer
  BTC.transfer(from_acc, to_acc, amount)  # Returns 1 for success, -1 for failure
  
  # Exchange
  BTC.exchange(btc_acc, eth_acc, ETH, amount)  # Cross-chain transaction
  ```

## 3. Implementation Details

### Main Components

#### MyBlock Class
```python
class MyBlock:
    def __init__(self, transaction = ()):
        self.transaction = transaction
        self.next = None
```
- Represents a single block in the chain
- Stores transaction type and arguments
- Implements linked list structure

#### MyBlockChain Class
```python
class MyBlockChain:
    def __init__(self, name):
        self.head = None
        self.chainName = name
        self.lock = threading.Lock()
```
- Manages the blockchain operations
- Implements thread-safe transactions
- Handles remote method calls

### Key Methods
- `createAccount(amount)`: Creates new account with initial balance
- `transfer(accfrom, to, amount)`: Handles intra-chain transfers
- `exchange(accFrom, to, toChain, amount)`: Manages inter-chain exchanges
- `calculateBalance(accId)`: Computes current balance for an account

## 4. Usage Instructions

### Requirements
- Python 3.x
- Pyro4 library
- Running Pyro4 name server

### Installation
```bash
pip install Pyro4
```

### Starting the System
1. Start the Pyro4 name server:
```bash
python -m Pyro4.naming
```

2. Start the BTC server:
```bash
python BTCServer.py
```

3. Start the ETH server:
```bash
python ETHServer.py
```

4. Run client operations:
```bash
python firstClient.py
# or
python secondClient.py
```

## 5. Error Handling

The system handles various error conditions:

- Non-existent accounts
- Insufficient funds
- Invalid transactions
- Concurrent access conflicts
- Network communication errors

Error handling mechanisms:
- Return value -1 for failed operations
- Thread locking for atomic operations
- Transaction validation before execution

## 6. Example Session

### Basic Operations
```python
# Create BTC account
BTC = Pyro4.Proxy("PYRONAME:BTC")
acc1 = BTC.createAccount(100)
print(f"Created BTC account: {acc1}")

# Check balance
bal = BTC.calculateBalance(acc1)
print(f"Balance: {bal}")

# Perform transfer
if bal > 20:
    result = BTC.transfer(acc1, 1, -60)
    print(f"Transfer result: {result}")

# View chain state
BTC.printChain()
```

### Cross-Chain Exchange
```python
# Create ETH account
ETH = Pyro4.Proxy("PYRONAME:ETH")
e1 = ETH.createAccount(30)

# Perform exchange
BTC.exchange(acc1, e1, ETH, -20)

# View both chains
BTC.printChain()
ETH.printChain()
```

Note: The system maintains consistency across distributed nodes and ensures atomic transactions through thread-safe operations.
