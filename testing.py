from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
   return "HELLO NAPIER", 404

if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
import unittest
import testing

class TestingTest(unittest.TestCase):
   def test_root(self):
      self.app = testing.app.test_client()
      out = self.app.get('/')
      assert '200 OK' in out.status
      assert 'charset=utf-8' in out.content_type
      assert 'text/html' in out.content_type

if __name__ == "__main__":
   unittest.main()
