from dataclasses import dataclass

@dataclass
class Chunk:
    id              : int
    unit_ids        : list[int]
    text            : str