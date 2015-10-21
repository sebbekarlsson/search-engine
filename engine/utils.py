

def get_filename(url):
    try:
        return url.split('/')[-1]
    except:
        return None

def get_dir(url):
    filename = get_filename(url)
    if filename is not None:
        return url.replace(filename, '')
    else:
        return url