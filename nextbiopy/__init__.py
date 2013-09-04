try:
    from ._version import __version__ as v
    __version__ = v
    del v
except ImportError:
    __version__ = "UNKNOWN"
