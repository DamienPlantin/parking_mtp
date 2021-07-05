import unittest
from tests import app


class BaseTest(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    self.app = app.test_client()
