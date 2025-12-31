"""
============================================================
Name:        Ashwin Nathan
Date:        December 29, 2025
Project:     Bell State Creation and Measurement (Qiskit)

Purpose:
--------
This script demonstrates the creation, visualization, and
measurement of a two-qubit entangled quantum state (Bell state)
using IBM Qiskit.

Description:
------------
The program performs the following steps:
1. Initializes a two-qubit quantum circuit.
2. Applies a Hadamard gate followed by a CNOT gate to create
   quantum entanglement between the qubits.
3. Simulates the quantum state using a statevector simulator
   and visualizes the qubits on the Bloch sphere.
4. Measures the entangled state using a QASM simulator.
5. Displays a histogram of the measurement outcomes, showing
   the characteristic correlations of a Bell state.

This example highlights foundational quantum computing concepts
including superposition, entanglement, statevector simulation,
and probabilistic measurement outcomes.

Technologies Used:
------------------
- Python
- Qiskit
- Qiskit Aer
- Matplotlib

============================================================
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
from qiskit_aer import Aer
from math import pi
import matplotlib.pyplot as plt

# Create a 2-qubit quantum circuit
circuit = QuantumCircuit(2)

# Apply Hadamard and CNOT gates to create entanglement
circuit.h(0)
circuit.cx(0, 1)
print(circuit)

# Statevector simulation (pre-measurement)
simulator = Aer.get_backend('statevector_simulator')
job = simulator.run(circuit)
result = job.result()
statevector = result.get_statevector(circuit)

# Visualize the quantum state on the Bloch sphere
plot_bloch_multivector(statevector)
plt.show()

# Measure all qubits
circuit.measure_all()

# QASM simulation (measurement outcomes)
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(circuit)
result = job.result()
counts = result.get_counts(circuit)

# Plot measurement histogram
plot_histogram(counts)
plt.show()
