"""
============================================================
Name:        Ashwin Nathan
Date:        December 28, 2025
Project:     Two-Bit Quantum Adder (Sum and Carry)

Purpose:
--------
This script demonstrates how fundamental arithmetic logic can be
implemented using quantum gates by constructing a two-bit quantum
adder that computes a SUM and CARRY-OUT from two input bits.

Description:
------------
The program builds a four-qubit quantum circuit where:
- Qubits 0 and 1 represent the input bits
- Qubit 2 stores the SUM output
- Qubit 3 stores the CARRY-OUT output

The circuit uses:
- CNOT (CX) gates to compute the XOR-based sum.
- A Toffoli (CCX) gate to compute the carry bit.
- Measurement operations to read the sum and carry into classical bits.

The circuit is executed using Qiskit's BasicSimulator backend, and the
measurement results are decoded to display the SUM and CARRY-OUT values
explicitly.

This example highlights core quantum computing concepts including
multi-qubit logic, controlled operations, reversible computation,
and the relationship between classical arithmetic and quantum circuits.

Technologies Used:
------------------
- Python
- Qiskit
- Qiskit Aer
- Qiskit BasicProvider
- Matplotlib

============================================================
"""

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit import transpile
from qiskit.providers.basic_provider import BasicProvider

# Create a 4-qubit quantum circuit with 2 classical bits
circuit = QuantumCircuit(4, 2)

# Initialize input bits a = 1, b = 1
circuit.x([0, 1])
circuit.barrier()

# Compute SUM and CARRY-OUT
circuit.cx(0, 2)        # SUM
circuit.cx(1, 2)
circuit.ccx(0, 1, 3)    # CARRY

circuit.barrier()

# Measure SUM and CARRY into classical bits
circuit.measure(2, 0)   # SUM -> c0
circuit.measure(3, 1)   # CARRY -> c1

print(circuit)

# Execute circuit using BasicSimulator
provider = BasicProvider()
backend = provider.get_backend("basic_simulator")

compiled = transpile(circuit, backend)
job = backend.run(compiled, shots=1)
result = job.result()

counts = result.get_counts()
bitstring = next(iter(counts))   # Format: c1c0

sum_bit = bitstring[1]           # c0
carry_bit = bitstring[0]         # c1

print(f"SUM is {sum_bit}")
print(f"CARRY-OUT is {carry_bit}")
