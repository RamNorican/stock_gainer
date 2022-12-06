import re

response_keys = {
    'Symbol': 'Symbol',
    'Name': 'Name',
    'Price (Intraday)': 'Price',
    'Change': 'Change',
    '% Change': 'Change_Per',
    'Volume': 'Volume',
    'Avg Vol (3 month)': 'Volume_Avg',
    'Market Cap': 'Market_Cap',
    'PE Ratio (TTM)': 'PE_Ratio',
    '52 Week Range': 'Week_Range_52'
    }

NUMERIC_KEYS = ["Price", "Change", "Change_Per"]


def special_str_to_int(res_dict):
    """
    Converts special strings to int ignoring special charecters
    """
    for key, val in res_dict.items():
        if key in NUMERIC_KEYS and isinstance(val, str):
            pattern = re.compile("[^0-9\.]")
            res_dict[key] = float(re.sub(pattern, "", val))
    return res_dict


def update_keys(result_keys):
    for key, val in response_keys.items():
        if key != val:
            result_keys[val] = result_keys[key]
            result_keys.pop(key)
    return result_keys


