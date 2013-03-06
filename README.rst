print_json_middleware
=====================

JSON prettyprinter WSGI middleware

Handy for viewing JSON payloads which would otherwise be downloaded by your web browser (due to the Content-Type response header being set to an unrecognized type like "application/json").

If a special query parameter (by default "pj", short for "Print JSON") is found in the query string, assume the response body contains JSON data which should be "printed" to the response by setting the response Content-Type to "text/plain".

Example usage::

    http://foo.org/some/json?pj

If the parameter has a positive integer value, prettyprint the JSON (sort the keys and treat the parm value as an indent value).

Example usage::

    http://foo.org/some/json?pj=2

Note that the parameter is removed from the request query string before the middleware invokes the wrapped application.

Setup
-----

If using Paster, edit your .ini file and add a new filter section::

    [filter:print_json]
    use = egg:print_json_middleware#print_json

Then find the application section (typically under the header ``[app:main]``) and add::

    filter-with = print_json

If you'd rather use some other parameter name than "pj", specify it in the ``[filter:print_json]`` section::

    parm = whatever

As an alternative to Paster configuration, you could do the application wrapping in Python code::

    from print_json_middleware import PrintJsonMiddleware
    application = PrintJsonMiddleware(application)

If you'd rather use some other parameter name than "pj", pass it as a second argument::

    application = PrintJsonMiddleware(application, "whatever")
