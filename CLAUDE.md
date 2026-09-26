# Qyphos

Qyphos is a high-performance, matrix-free classical quantum computing simulator — it can simulate Grover's algorithm and other circuits on CPU and (optionally) GPU backends, with optional noise models and a transpiler/optimizer. The package exposes a Python library (`qyphos.core.simulator.QyphosSimulator`, `qyphos.core.circuit.QuantumCircuit`), a CLI (`cli.py`), an interactive Streamlit dashboard (`app.py`), and a quick tensor smoke test (`test_tensor.py`).

## Build / Test / Lint Commands

- Install: `pip install -r requirements.txt` (numpy, scipy, numba, psutil, streamlit, plotly, pandas, quimb, autoray); install CuPy separately for GPU support
- Build: not applicable (interpreted Python)
- Test: `python test_tensor.py` (basic backend smoke test); no formal pytest suite is wired in
- Lint: not configured
- Dev / run:
  - CLI: `python cli.py` (or `python -m cli` depending on entry point)
  - Streamlit dashboard: `streamlit run app.py`
  - Library: `from qyphos import QyphosSimulator, QuantumCircuit`

## Code Style Rules

- Language/version: Python 3.10+
- Paradigm: package layout with subpackages — `core/`, `backends/`, `benchmarks/`, `noise/`, `transpiler/`, `utils/`; the public API is the `qyphos` top-level package
- Types: type hints on the public `QyphosSimulator` and `QuantumCircuit` classes
- Formatting: PEP 8 (no formatter configured)
- Imports / module style: `from qyphos.core.simulator import QyphosSimulator` style; relative imports inside subpackages
- Dependencies: numerical Python stack (numpy, scipy, numba, quimb, autoray), plus streamlit/plotly/pandas for the dashboard

## Verification Criteria

Before claiming any task done, Claude MUST:
1. Run `python -c "from qyphos.core.simulator import QyphosSimulator; from qyphos.core.circuit import QuantumCircuit"` to confirm the public API imports.
2. Run `python test_tensor.py` and confirm it prints `Probabilities: ...` without an unhandled exception.
3. Confirm `pip install -r requirements.txt` succeeds in a clean venv.
4. Report the exact commands run and their outcomes in the final message.

## GitHub account rule (AGENCY-ACCOUNT-RULE)
This folder is a PERSONAL project of boblio-max. For ANY GitHub operation
(gh commands, git push/pull, releases), the active account MUST be
`boblio-max` — NEVER the Storefront Web agency account.
Check first: `gh auth status`. If another account is active, run
`gh auth switch --user boblio-max` before proceeding.
