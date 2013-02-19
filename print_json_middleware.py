import json
from webob import Request

class PrintJsonMiddleware(object):
    """ JSON prettyprinter WSGI middleware.
    If a special query parameter (by default "pj", for "Print JSON")
    is found in the query string, assume the response body contains JSON data
    which should be "printed" to the response as text/plain.
    If the parameter has a positive integer value, treat it as an indent value
    and sort the keys.
    Note that the parameter is removed from the request query string
    before the middleware invokes the wrapped application.
    """

    def __init__(self, app, parm='pj'):
        self.app = app
        self.parm = parm

    def __call__(self, environ, start_response):
        pretty = False
        indent = 0
        req = Request(environ)
        if self.parm in req.GET:
            pretty = True
            try:
                indent = int(req.GET.get(self.parm, 0))
            except:
                pass
            # Rewrite the query_string removing parm.
            parms = []
            for parm in req.query_string.split('&'):
                name = parm.split('=')[0]
                if name != self.parm:
                    parms.append(parm)
            req.query_string = '&'.join(parms)
        resp = req.get_response(self.app)
        if pretty:
            resp.content_type = 'text/plain'
            if indent > 0:
                resp.body = json.dumps(json.loads(resp.body),
                                       indent=indent,
                                       sort_keys=True)
        return resp(environ, start_response)
