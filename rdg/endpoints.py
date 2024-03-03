from fastapi import APIRouter
from rdg.functions import *
from rdg.models import *

router = APIRouter()

@router.post("/random-int")
async def get_random_int(data: IntData):
    '''
    Generates a list of random integers from the specified range.

    Args:\n
        data (IntData): 
            range_from (int): 
                An object containing the starting value of the numeric range for the generated integers.
            range_to (int): 
                An object containing the ending value of the numeric range for the generated integers.
            amount (int, optional): 
                The amount of numbers to generate.
            
    Returns:\n
        dict: 
            A dictionary containing the randomly generated list of integers from the specified range.
    '''
    result = await generate_int(data.range_from, data.range_to, data.amount)
    return {"random_numbers": result}



@router.post("/random-float")
async def get_random_float(data: FloatData):
    '''
    Generates a list of random floating-point numbers from the specified range.

    Args:\n
        data (FloatData):
            range_from (float): 
                An object containing the starting value of the numeric range for the generated floating-point numbers.
            range_to (float): 
                An object containing the ending value of the numeric range for the generated floating-point numbers.
            decimal_places (int): 
                The number of decimal places (up to 14) for the generated floating-point numbers.
            amount (int, optional): 
                The amount of numbers to generate.
            
    Returns:\n
        dict: 
            A dictionary containing the randomly generated list of floating-point numbers from the specified range.
    '''
    result = await generate_float(data.range_from, data.range_to, data.decimal_places, data.amount)
    return {"random_numbers": result}

@router.post("/random-date")
async def get_random_date(data: DateData):
    """
    Generates a list of random datetime objects between two datetime objects.

    Args:\n
        data (DateData):
            range_from (datetime): 
                An object containing the starting datetime for the generated dates.
            range_to (datetime): 
                An object containing the ending datetime for the generated dates.
            amount (int, optional): 
                The amount of datetime objects to generate.

    Returns:\n
        list: 
            A list containing the randomly generated datetime objects.
    """
    delta = data.range_to - data.range_from
    random_seconds = np.random.randint(delta.total_seconds(), size=data.amount)
    random_dates = [data.range_from + timedelta(seconds=int(td)) for td in random_seconds]
    
    return random_dates