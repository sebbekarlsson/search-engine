

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

def teaserify(text, term):
    if len(text) >= 128:

        try:
            content_part_1 = text.split(term)[0]
            content_part_2 = text.split(term)[1]
        except IndexError:
            content_part_1 = text
            content_part_2 = ''

        if len(content_part_1) > 128:
            content_part_1 = content_part_1[-128:]
        if len(content_part_2) > 128:
            content_part_2 = content_part_2[-128:]

        if term not in content_part_1 or term not in content_part_2:
            text = content_part_1 + term + content_part_2

    return text