# code = int(type('Enter a status code'));

def statusCode(code):
    match code:
        case 200:
            return 'Success'
        case 404:
            return 'not found'
        case _:
            return 'unknown';

c = statusCode(300);
print(c)