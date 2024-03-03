import numpy as np

async def generate_int(range_from: int, range_to: int, amount: int) -> list[int]:
    return np.random.randint(range_from, range_to, size=amount).tolist()

async def generate_float(range_from: float, range_to: float, decimal_places: int, amount: int) -> list[float]:
    return [round(x, decimal_places) for x in np.random.uniform(range_from, range_to, size=amount)]