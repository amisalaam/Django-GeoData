try:
    from .countries import Country
except ImportError:
    Country = None

try:
    from .states import State
except ImportError:
    State = None

try:
    from .districts import District
except ImportError:
    District = None
