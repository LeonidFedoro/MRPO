from dataclasses import dataclass
from datetime import datetime

@dataclass
class Gift:
    id: int
    name: str
    value: float
    timestamp: datetime
