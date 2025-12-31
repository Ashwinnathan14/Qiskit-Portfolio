"""
============================================================
Name:        Ashwin Nathan
Date:        December 26, 2025
Project:     Quantum State Preparation with Target Probabilities

Purpose:
--------
This script demonstrates how to prepare a multi-qubit quantum
state with specific, non-uniform measurement probabilities using
single-qubit rotations and superposition in Qiskit.

Description:
------------
The program constructs a three-qubit quantum circuit designed
to produce the following measurement probabilities:

- 37.5% chance of |001⟩
- 37.5% chance of |011⟩
- 12.5% chance of |101⟩
- 12.5% chance of |111⟩

This is achieved by:
1. Applying a parameterized Y-rotation (Ry) to bias one qubit’s
   probability amplitudes.
2. Using a Hadamard gate to place another qubit into equal
   superposition.
3. Initializing the final qubit deterministically to |1⟩.
4. Measuring all qubits and verifying the resulting probability
   distribution using a histogram.

This example highlights key quantum computing concepts including
state preparation, amplitude-to-probability mapping, and the
relationship between single-qubit rotations and measurement
outcomes.

Technologies Used:
------------------
- Python
- Qiskit
- Qiskit Aer
- Matplotlib

============================================================
"""

# State Prep problem

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
from qiskit_aer import Aer
from math import pi
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Create a 3-qubit quantum circuit
circuit = QuantumCircuit(3)

# Prepare the desired quantum state
circuit.ry(pi / 3, 2)   # Bias qubit 2 probabilities (3/4 vs 1/4)
circuit.h(1)            # Create equal superposition on qubit 1
circuit.x(0)            # Set qubit 0 deterministically to |1⟩

# Measure all qubits
circuit.measure_all()
print(circuit)

# Simulate measurement outcomes
simulator = Aer.get_backend("qasm_simulator")
job = simulator.run(circuit)
result = job.result()
counts = result.get_counts(circuit)

# Display results
print(counts)
plot_histogram(counts)
plt.show()
