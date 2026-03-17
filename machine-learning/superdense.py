from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# 1. Setup: 2 Qubits, 2 Classical Bits
qr = QuantumRegister(2, name="q")
cr = ClassicalRegister(2, name="bits")
qc = QuantumCircuit(qr, cr)

# --- STEP 1: Create Entanglement (The Shared Resource) ---
# This "links" Alice (q0) and Bob (q1)
qc.h(0)
qc.cx(0, 1)
qc.barrier()

# --- STEP 2: Alice Encodes her 2-bit message ('11') ---
# Alice only has access to q0. To send '11', she applies Z and X.
# Message Map: '00'=None, '01'=X, '10'=Z, '11'=ZX
qc.z(0)
qc.x(0)
qc.barrier()

# --- STEP 3: Alice sends her qubit (q0) to Bob ---
# (In simulation, Bob now "owns" both q0 and q1)

# --- STEP 4: Bob Decodes the message ---
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# --- STEP 5: Bob Measures ---
qc.measure(qr, cr)

# Run simulation
sim = AerSimulator()
result = sim.run(qc).result()
print(f"Bob received the message: {result.get_counts()}")

# Draw circuit
qc.draw("mpl")
plt.show()
