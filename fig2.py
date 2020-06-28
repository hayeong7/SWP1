from cgi import parse_qs
from template2 import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    Sum = -1 
    Multi = -1 

    try:
        a, b = int(a), int(b)
        Sum = a+b
        Multi = a*b
    except ValueError:
        Sum = "write the integer"
        Multi = "write the integer"
    response_body = html % {
        'Sum': Sum,
        'Multi': Multi,        
    }
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body] 
