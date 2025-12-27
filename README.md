# Qyphos

A high-performance **classical quantum computing simulator** designed to efficiently simulate quantum circuits, including Grover’s algorithm and other advanced quantum algorithms, on CPU and GPU.

---

## 🚀 Features

- **Matrix-free statevector engine** – Simulate larger qubit counts (~30+) without storing full 2ᴺ×2ᴺ matrices.  
- **CPU & GPU support** – Accelerated backends via Numba (CPU) and CuPy (NVIDIA GPUs).  
- **Noise modeling** – Includes depolarizing, damping, and customizable noise models for realistic simulations.  
- **Circuit optimization** – Transpiler/optimizer reduces gate count and runtime for efficient simulation.  
- **OpenQASM 2.0 support** – Import and export circuits compatible with other quantum frameworks.  
- **Flexible API** – Use via Python library, CLI, or interactive Streamlit dashboard.

---

## 💻 Installation

```bash
git clone https://github.com/boblio-max/Qyphos.git
cd Qyphos
pip install -r requirements.txt
```

## Python API
```python
from qyphos import Qyphos

# Initialize simulator with 5 qubits
sim = Qyphos(qubits=5, backend="cpu")

# Create a Grover's search circuit
sim.grover(target_state="10101")

# Run simulation
result = sim.run(shots=1024)

print(result)
```

## Example
```python
sim = Qyphos(qubits=3)
sim.grover(target_state="110")
result = sim.run(shots=1000)
print(result)
# Output: {'110': 950, '000': 25, '001': 25}
```
##🛠 Contributing

Contributions are welcome! Please open an issue or pull request with improvements.
Areas to contribute:

Backend optimizations (CPU/GPU)

Additional noise models

Circuit visualization and dashboard improvements

Benchmarking scripts and testing

