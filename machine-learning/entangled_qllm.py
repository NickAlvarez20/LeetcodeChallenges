import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.circuit import Parameter
import matplotlib.pyplot as plt

# 1. Setup 3 Qubits (Word 1, Word 2, Word 3)
theta1 = Parameter("θ1")
theta2 = Parameter("θ2")
theta3 = Parameter("θ3")
qc = QuantumCircuit(3, 3)

# WORD 1: The Subject ("Quantum")
qc.rx(theta1, 0)

# LINK 1: If Word 1 is 1, Word 2 becomes 1 ("Computing")
qc.cx(0, 1)
qc.ry(theta2, 1)

# LINK 2: If Word 2 is 1, Word 3 becomes 1 ("Success")
qc.cx(1, 2)
qc.ry(theta3, 2)

# MEASURE ALL 3
qc.measure([0, 1, 2], [0, 1, 2])


# 2. Inference Function
def run_3word_model(w1, w2, w3):
    bound_qc = qc.assign_parameters({theta1: w1, theta2: w2, theta3: w3})
    sim = AerSimulator()
    counts = sim.run(bound_qc, shots=1000).result().get_counts()

    # We look for '111' (Triple Positive)
    success_rate = counts.get("111", 0) / 1000
    return success_rate, counts


# 3. TEST: Start with a "Strong" first word (np.pi)
prob, raw_counts = run_3word_model(np.pi, 0, 0)

print("\n--- 3-Word Quantum LLM Results ---")
print(f"Sentence: 'Quantum Computing Success'")
print(f"Probability of '111' State: {prob*100:.1f}%")
print(f"Raw Counts: {raw_counts}")

# Draw the 3-qubit chain
qc.draw("mpl")
plt.show()
