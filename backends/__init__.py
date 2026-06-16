from .base_backend import BaseBackend
from .numpy_backend import NumpyBackend
from .cupy_backend import CupyBackend
from .tensor_backend import TensorNetworkBackend

def get_backend(name: str) -> BaseBackend:
    if name == 'numpy':
        return NumpyBackend()
    elif name == 'cupy':
        return CupyBackend()
    elif name == 'tensor':
        return TensorNetworkBackend()
    elif name == 'auto':
        return TensorNetworkBackend()  # Default to new tensor backend
    else:
        raise ValueError(f"Unknown backend: {name}")
