print_json_middleware
=====================

JSON prettyprinter WSGI middleware

Handy for viewing JSON payloads which would otherwise be downloaded (due to Content-Type: "application/json").

If a special query parameter (by default "pj", short for "Print JSON") is found in the query string, assume the response body contains JSON data which should be "printed" to the response as text/plain.

If the parameter has a positive integer value, treat it as an indent value and sort the keys.

The parameter is removed from the request query string before the middleware invokes the wrapped application.
