import numpy as np
import string
from rdg.data import phones
async def generate_int(range_from: int, range_to: int, amount: int) -> list[int]:
    return np.random.randint(range_from, range_to, size=amount).tolist()

async def generate_float(range_from: float, range_to: float, decimal_places: int, amount: int) -> list[float]:
    return [round(x, decimal_places) for x in np.random.uniform(range_from, range_to, size=amount)]

async def generate_email(length: int, domain: str, amount: int) -> list[str]:
    chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    return [''.join(np.random.choice(chars, length))+domain for _ in range(amount)]
    
async def generate_phone(country: str, amount: int) -> list[int]:
    l = phones[country]
    return np.random.randint(int(l*'1'), int(l*'9'), size=amount).tolist()