
def validate_url_type(url):
    if isinstance(url, (str)):
        return url.strip()
    if isinstance(url, (bytearray, bytes)):
        pass



def validate_regex_url(url):
    pass

def validate_str_url(url):
    pass