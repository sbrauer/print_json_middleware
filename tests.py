import unittest
from webtest import TestApp

def _get_demo_app():
    import json
    def demo_app(environ, start_response):
        start_response("200 OK", [('Content-Type','application/json')])
        return [json.dumps(dict(
                foo='Hello',
                bar=['lorem', 'ipsum'],
                qs=environ['QUERY_STRING']
                ))]
    return demo_app

class TestPJ(unittest.TestCase):

    def setUp(self):
        from print_json_middleware import PrintJsonMiddleware
        demo_app = _get_demo_app()
        mw_app = PrintJsonMiddleware(demo_app)
        self.test_app = TestApp(demo_app)
        self.test_mw_app = TestApp(mw_app)

    def test_no_parm(self):
        normal_resp = self.test_app.get('/')
        mw_resp = self.test_mw_app.get('/')
        self.assertEqual(mw_resp.content_type, 'application/json')
        self.assertEqual(normal_resp.body, mw_resp.body)

    def test_empty_parm(self):
        normal_resp = self.test_app.get('/?pj')
        mw_resp = self.test_mw_app.get('/?pj')
        self.assertEqual(mw_resp.content_type, 'text/plain')
        self.assertNotEqual(normal_resp.body, mw_resp.body)
        self.assertEqual(normal_resp.json_body['qs'], 'pj')
        self.assertEqual(mw_resp.json_body['qs'], '')
        json_body = normal_resp.json_body
        json_body['qs'] = ''
        self.assertEqual(mw_resp.json_body, json_body)

    def test_positive_parm(self):
        normal_resp = self.test_app.get('/?meh=123&pj=2&baz=feh')
        mw_resp = self.test_mw_app.get('/?meh=123&pj=2&baz=feh')
        self.assertEqual(mw_resp.content_type, 'text/plain')
        self.assertNotEqual(normal_resp.body, mw_resp.body)
        self.assertEqual(normal_resp.json_body['qs'], 'meh=123&pj=2&baz=feh')
        self.assertEqual(mw_resp.json_body['qs'], 'meh=123&baz=feh')
        self.assertEqual(mw_resp.body, '''{
  "bar": [
    "lorem", 
    "ipsum"
  ], 
  "foo": "Hello", 
  "qs": "meh=123&baz=feh"
}''')

if __name__ == '__main__':
    unittest.main()
