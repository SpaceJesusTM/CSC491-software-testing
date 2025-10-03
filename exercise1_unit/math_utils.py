import math
from numbers import Real
import numpy as np

def add(a: int, b: int) -> int:
    """Return a + b."""
    # if math.isnan(a) or math.isnan(b):
    # add(True, 1) should raise TypeError, not return 2
    if not (isinstance(a, Real) or isinstance(b, Real)):
        raise TypeError("add() only supports numeric types")
    # should reject bools too
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("add() only supports numeric types")
    return a + b

def div(a: float, b: float) -> float:
    """Return a / b. Raise ValueError if b == 0."""
    if not math.isfinite(b):
        raise ValueError("division by non-finite value")
    if b == 0:
        raise ValueError("division by zero")
    return a / b
    # TODO: to uncomment the below line and comment the above line and observe the effects
    # return float(np.float32(a) / np.float32(b))

def clamp(x: float, low: float, high: float) -> float:
    """Confine x to [low, high]."""
    if math.isnan(x) or math.isnan(low) or math.isnan(high):
        raise ValueError("clamp() does not support NaN values")
    if math.isinf(x) or math.isinf(low) or math.isinf(high):
        raise ValueError("clamp() does not support infinite values")
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(x, high))
