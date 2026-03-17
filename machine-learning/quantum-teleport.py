from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# 1. Setup registers - We MUST include all of them in the QuantumCircuit call
qr = QuantumRegister(3, name="q")
crz = ClassicalRegister(1, name="crz")
crx = ClassicalRegister(1, name="crx")
crb = ClassicalRegister(1, name="bob")

# IMPORTANT: All 4 registers must be listed here
qc = QuantumCircuit(qr, crz, crx, crb)

# Step 1: Prepare the "Message" (State |1>) on Qubit 0
qc.h(0)
qc.barrier()

# Step 2: Create Entanglement (Bell Pair) between Qubit 1 and Qubit 2
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Step 3: Alice's Bell Measurement
qc.cx(0, 1)
qc.h(0)
qc.barrier()
qc.measure(qr[0], crz[0])  # Measure q0 into crz
qc.measure(qr[1], crx[0])  # Measure q1 into crx
qc.barrier()

# Step 4: Bob's Conditional Corrections
with qc.if_test((crx, 1)):
    qc.x(2)
with qc.if_test((crz, 1)):
    qc.z(2)
qc.barrier()

# Step 5: 
qc.measure(qr[2], crb[0])

# Run simulation
sim = AerSimulator()
job = sim.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("\n--- Teleportation Results ---")
print("Format: 'Bob_Bit Alice_Bits'")
print(counts)

# Draw the circuit
qc.draw("mpl")
plt.show()
