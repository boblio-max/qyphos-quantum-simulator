from qyphos.core.simulator import QyphosSimulator
from qyphos.core.circuit import QuantumCircuit

def test_tensor_backend():
    print("Initializing simulator with tensor backend...")
    sim = QyphosSimulator(backend_name='tensor')
    
    circuit = QuantumCircuit(3)
    circuit.h(0)
    circuit.h(1)
    circuit.mcx([0, 1], 2) # Toffoli
    
    print("Running circuit...")
    result = sim.run(circuit)
    print("Probabilities:", result['final_probabilities'])

if __name__ == "__main__":
    test_tensor_backend()
