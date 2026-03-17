from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Create Quantum Circuit with 1 Qubit and 1 Classical bit
qc = QuantumCircuit(1, 1)

# 2. Put the Qubit in Superposition (The "Quantum" step)
qc.h(0)

# 3. Measure the Qubit and store the result in the Classical bit
qc.measure(0, 0)

# 4. Simulate the circuit 1000 times
simulator = AerSimulator()
job = simulator.run(qc, shots=1000000)
result = job.result()

# 5. Get the results (counts of 0s and 1s)
counts = result.get_counts()
print(f"Quantum Results: {counts}")

# 6. Visualize the "Fairness" of the Quantum Coin Toss
plot_histogram(counts)
plt.title("Quantum Random Bit Distribution")
plt.show()

# 7. Draw the actual circuit diagram
qc.draw('mpl')
plt.show()