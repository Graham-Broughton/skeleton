import os
from dataclasses import dataclass

base = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(base, 'data')
submissions = os.path.join(base, 'submissions')


@dataclass
class CFG:
    BASE_PATH: str = base
    DATA_PATH: str = data
    SUB_PATH: str = submissions
    NROWS: int = 100
    NCOLS: int = 30
    