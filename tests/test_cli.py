import unittest
import pytest
from snucovery.cli import Arguments


class TestCli(unittest.TestCase):
    def test_init_args(self):
        args = Arguments()
        self.assertTrue(str(args.parser.print_help()))
        self.assertIsInstance(args, object)
