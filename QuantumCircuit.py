"""
============================================================
Name:        <YOUR NAME HERE>
Date:        December 20, 2025
Project:     Basic Single-Qubit Quantum Circuit (Superposition)

Purpose:
--------
This script demonstrates the creation, measurement, and
visualization of a basic single-qubit quantum circuit using
Qiskit. It is a very basic introductory example of creating
a basic circuit using a bit and qubit, in which the qubit is 
then put into quantum superposition using a Hadamard gate.

Description:
------------
The program performs the following steps:
1. Creates a single-qubit quantum register and a single classical
   register.
2. Applies a Hadamard (H) gate to place the qubit into an equal
   superposition of |0⟩ and |1⟩.
3. Simulates measurement outcomes using a QASM simulator and
   visualizes the resulting probability distribution with a
   histogram.
4. Simulates the quantum state prior to measurement using a
   statevector simulator.
5. Visualizes the quantum state on the Bloch sphere to illustrate
   the geometric representation of superposition.

This program highlights fundamental quantum computing concepts
including quantum registers, superposition, statevector
simulation, and the probabilistic nature of quantum measurement.

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
import matplotlib.pyplot as plt

# Create quantum and classical registers
qr = QuantumRegister(1)
cr = ClassicalRegister(1)

# Build the quantum circuit
circuit = QuantumCircuit(qr, cr)
circuit.h(qr)            # Apply Hadamard gate
circuit.measure(qr, cr) # Measure the qubit

# QASM simulation (measurement outcomes)
simulator = Aer.get_backend("qasm_simulator")
job = simulator.run(circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

print(counts)
plot_histogram(counts)
plt.show()

# Statevector simulation (pre-measurement state)
simulator2 = Aer.get_backend("statevector_simulator")
job2 = simulator2.run(circuit)
result2 = job2.result()
statevector = result2.get_statevector(circuit)

print(statevector)
plot_bloch_multivector(statevector)
plt.show()
