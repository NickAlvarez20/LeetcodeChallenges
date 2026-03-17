import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.circuit import Parameter

# 1. Create the Mini-Corpus (100 labeled samples)
# Features (X) are "Phase Angles", Labels (y) are 0 (Neg) or 1 (Pos)
X = np.concatenate([np.random.uniform(0, 0.5, 50), np.random.uniform(2.5, 3.1, 50)])
y = np.concatenate([np.zeros(50), np.ones(50)])

# 2. Setup the Quantum "Brain"
theta = Parameter("θ")
qc = QuantumCircuit(1, 1)
qc.rx(theta, 0)
qc.measure(0, 0)


def run_quantum_model(angle):
    bound_qc = qc.assign_parameters({theta: angle})
    counts = AerSimulator().run(bound_qc, shots=100).result().get_counts()
    # Return probability of being '1'
    return counts.get("1", 0) / 100


# 3. Simple Training Loop
learned_weight = 0.1  # Starting guess
learning_rate = 0.5

print("Starting Training...")
for epoch in range(5):
    total_error = 0
    for i in range(len(X)):
        prediction = run_quantum_model(X[i] * learned_weight)
        error = y[i] - prediction
        learned_weight += error * learning_rate * 0.01  # Nudge the weight
        total_error += abs(error)

    print(f"Epoch {epoch+1}: Avg Error = {total_error/100:.4f}")

# 4. Test the "Learned" Model
test_val = 2.9  # A "Positive" angle
result = run_quantum_model(test_val * learned_weight)
sentiment = "Positive" if result > 0.5 else "Negative"

print(f"\nTest Input Angle: {test_val}")
print(f"Predicted Sentiment: {sentiment} (Confidence: {result*100:.1f}%)")
