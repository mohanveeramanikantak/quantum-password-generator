from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import string


def generate_quantum_bits(bits: int) -> str:
    circuit = QuantumCircuit(bits, bits)

    for i in range(bits):
        circuit.h(i)

    circuit.measure(range(bits), range(bits))

    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1).result()
    counts = result.get_counts()

    return list(counts.keys())[0]


def generate_password(length: int = 12) -> str:
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    for _ in range(length):
        quantum_bits = generate_quantum_bits(8)
        random_index = int(quantum_bits, 2) % len(characters)
        password += characters[random_index]

    return password


def check_strength(password: str) -> str:
    score = 0

    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*" for char in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"