import yaml
from pathlib import Path
from typing import Dict, Any

class Config:
    def __init__(self, config_path: str = "configs/default.yaml"):
        path = Path(config_path)
        if not path.is_absolute() and not path.exists():
            project_root = Path(__file__).resolve().parent.parent
            path = project_root / config_path
        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {path}")
        with path.open('r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file) or {}
    
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value != {} else default