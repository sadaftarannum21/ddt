import unittest

from src.framework.infra.tools import Tools


class ToolsUnitTest(unittest.TestCase):
    """
    ToolsUnitTest is an entity that...
    TODO: documentation for ToolsUnitTest.py
    """
    def setUp(self):
        self.obj = Tools()

    def audit_filter(self):
        with self.assertRaises(ValueError) as context:
            self.obj.filter(None)
        self.assertEqual(str(context.exception), "data can not be None")


if __name__ == '__main__':
    unittest.main()
