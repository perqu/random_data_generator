from fastapi import APIRouter
from rdg.functions import *
from rdg.models import *
from rdg.data import col_vars
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
    result = await generate_date(data.range_from, data.range_to, data.amount)
    return result

@router.post("/random-email")
async def get_random_email(data: EmailData):
    """
    Generates a list of random email addresses.

    Args:\n
        data (EmailData):
            length (int): 
                The length of the username part of the email addresses.
            domain (str): 
                The domain name for the email addresses.
            amount (int): 
                The amount of email addresses to generate.


    Returns:\n
        list: 
            A list containing the randomly generated email addresses.
    """
    emails = await generate_email(data.length, data.domain, data.amount)
    return emails

@router.post("/random-phone")
async def get_random_phone(data: PhoneData):
    """
    Generates a list of random phone numbers.

    Args:\n
        data (PhoneData):
            country (str): 
                The country name for pick exact phone number length.
            amount (int): 
                The amount of email addresses to generate.


    Returns:\n
        list: 
            A list containing the randomly generated email addresses.
    """
    phones = await generate_phone(data.country, data.amount)
    return phones

@router.post('/random-table')
async def get_random_table(data: TableData):
    """
    Generates a random table based on the provided TableData.

    Parameters:\n
        data (TableData): An object containing the code specifying the structure of the table.

    Returns:\n
        List[List]: A list of lists representing the generated random table.

    Example:\n
        First value represents number of rows.
        If code is "20[int](10)(20)[float](10)(20)(2)[date](2023-03-06)(2024-03-05)[email](7)(wp.pl)[phone](poland)", 
        it generates a random table with 5 columns and 20 rows:
        - The first column contains integers between 10 and 20.
        - The second column contains floats between 10 and 20.
        - The third column contains dates between 2023-03-06 and 2024-03-05.
        - The fourth column contains emails with 7 letters and "wp.pl" as domain.
        - The fifth column contains phones from Poland.

        [INT](from)(to)
        [FLOAT](from)(to)(decimals)
        [DATE](from)(to)
        [EMAIL](letters)(@domain)
        [phone](country)

    """
    try:
        code = data.code
        is_valid, message = is_valid_code(code)
        if not is_valid:
            return {"error": message}
        
        col_names = []
        cols = []
        num_cols = code.count('[')
        num_rows = int(code[:code.find('[')])
        for _ in range(num_cols):
            # Get column type
            c1 = code.find('[')+1
            c2 = code.find(']')

            variables = []

            col_type = code[c1:c2]
            col_names.append(col_type)
            code = code[c2+1:]

            var_types = col_vars[col_type]
            for vt in var_types:
                c11 = code.find('(')+1
                c12 = code.find(')')
                variable = code[c11:c12]
                code = code[c12+1:]
                if vt == 'i':
                    variable = int(variable)
                elif vt == 'f':
                    variable = float(variable)
                elif vt == 'd':
                    variable = datetime.strptime(variable, "%Y-%m-%d")
                else:
                    pass
                variables.append(variable)

            cols.append(await generate_functions[col_type](*variables, num_rows))
        return list(zip(*cols))
    except:
        return "Bad code"
