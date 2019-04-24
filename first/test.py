import unittest

from collections import OrderedDict
from first.main import load, store


class TestMap(unittest.TestCase):

    def test_load_good(self):
        lines = [
            "key1=1;key2=2",
            "other_key=qwertyuiop!",
            "yet_another_key=22;something=33",
            ""
        ]
        raw = "\n".join(lines)
        result = load(raw)
        self.assertEqual(len(result), 4)
        self.assertDictEqual(result[0], {"key1": "1", "key2": "2"})
        self.assertDictEqual(result[1], {"other_key": "qwertyuiop!"})
        self.assertDictEqual(result[2], {"yet_another_key": "22", "something": "33"})
        self.assertDictEqual(result[3], {})

    def test_load_good2(self):
        lines = ["key11=", "key21=12"]
        raw = "\n".join(lines)
        result = load(raw)
        self.assertDictEqual(result[0], {"key11": ""})
        self.assertDictEqual(result[1], {"key21": "12"})

    def test_load_empty(self):
        result = load("")
        self.assertEqual(result, [{}])

    def test_load_malformed(self):
        with self.assertRaises(ValueError):
            load("""key=1;""")

    def test_store_good(self):
        # so that we can assert on the string itself, without having to deal with the fact that
        # python dicts does not maintain order
        list_of_maps = [
            OrderedDict([("key1", "12")]),
            OrderedDict([("!!!", "zxcqweIO"), ("123", "456")]),
            OrderedDict()
        ]
        result = store(list_of_maps)
        expected_result = "\n".join([
            "key1=12",
            "!!!=zxcqweIO;123=456",
            ""
        ])
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
