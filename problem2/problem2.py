def date_format(date):
    year = date[-4:]
    month = date[0:2]
    day = date[3:5]
    return f"{year}-{month}-{day}"