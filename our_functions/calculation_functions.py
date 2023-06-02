import math


def calc_pythagoras(a: float, b: float, 
                    rounding:int=1,
                    return_both=False) -> float:
    '''
    Function to apply the Pythagoras theorem

    Params:
    * a (float): The a side of the triangle
    * b (float): The b side of the triangle

    Returns:
    * c: c side of the triangle
    '''
    c_2 = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_2)

    c_rounded = round(c, rounding)

    if return_both:
        return c_rounded, c
    else:
        return c_rounded


def contents_box(length: float, width: float, height: float) -> float:
    '''
    Function that returns the contents of a box:

    Params:
    * length
    * width
    * height

    Returns:
    * contents 
    '''
    content = length * width * height
    return content