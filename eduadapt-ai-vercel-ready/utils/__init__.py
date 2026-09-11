from .config import Config

__all__ = ["Config", "LearningVisualizer"]

def __getattr__(name):
    if name == "LearningVisualizer":
        from .visualization import LearningVisualizer
        return LearningVisualizer
    raise AttributeError(name)
