# Qyphos — matrix-free quantum circuit simulator

a classical simulator for quantum circuits that skips the giant matrices — matrix-free statevector evolution on CPU and GPU, with Grover's algorithm, noise models, a transpiler/optimizer, a CLI, and a Streamlit dashboard. real quantum computing is expensive; this lets you experiment for free.

## how it actually works

- `core/{circuit,simulator,oracles}.py` — `QuantumCircuit` builds the circuit, `QyphosSimulator` evolves the statevector without ever materializing the full 2^n × 2^n operators (that's the "matrix-free" part — it's what keeps memory from exploding)
- `backends/` — numpy (default), numba (JIT speed), CuPy (GPU)
- `noise/` — depolarizing/decoherence channels so results look like real hardware
- `transpiler/` — gate optimization passes
- `cli.py` — Grover `run`/`benchmark` commands; `app.py` — Streamlit + Plotly dashboard; `test_tensor.py` — backend smoke test

```bash
pip install -r requirements.txt  # numpy, scipy, numba, quimb, streamlit, plotly, pandas (+ cupy for GPU)
python test_tensor.py     # expect: Probabilities: ...
python cli.py             # Grover runs + benchmarks
streamlit run app.py      # dashboard
```

```python
from qyphos.core.simulator import QyphosSimulator
from qyphos.core.circuit import QuantumCircuit
```

## stack

Python, numpy/scipy/numba/quimb/autoray, Streamlit + Plotly. no formal pytest suite yet — `test_tensor.py` is the health check.
