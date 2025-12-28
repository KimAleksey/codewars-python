"""
https://www.codewars.com/kata/51646de80fd67f442c000013/train/python

Removes any duplicate query string parameters from the url (the first occurence should be kept)
Removes any query string parameters specified within the 2nd argument (optional array)
"""


def strip_url_params(url, params_to_strip=None) -> str:
    if len(url.split("?")) != 2:
        return url
    base_url = url.split("?")[0]
    params = url.split("?")[-1]
    if not params:
        return url
    param_dict = {}
    param_list = []
    for param in params.split("&"):
        key = param.split("=")[0]
        value = param.split("=")[-1]
        if not key in param_dict:
            if (not params_to_strip is None and key not in params_to_strip) or params_to_strip is None:
                param_dict[key] = value
                param_list.append((key, value))
    url = base_url + ("?" + '&'.join(param[0] + "=" + param[1] for param in param_list) if len(param_list) != 0 else "")
    return url