from dataclasses import dataclass

@dataclass(frozen=True)
class Gift:
    id: int
    name: str
    value: float
