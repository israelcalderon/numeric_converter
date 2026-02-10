import unittest

from collections import namedtuple

from numeric_converter.converter import (base_character, BaseNotSupported,
                                         base_10_to_r_int, base_10_to_r_dec,
                                         base_10_to_r)


class TestBaseCharacter(unittest.TestCase):

    def setUp(self) -> None:
        character_mock = namedtuple('CharacterMock', ['number', 'expected'])
        self.base_characters_mock = [character_mock(number=0, expected="0"),
                                     character_mock(number=1, expected="1"),
                                     character_mock(number=8, expected="8"),
                                     character_mock(number=10, expected="A"),
                                     character_mock(number=15, expected="F"),
                                     character_mock(number=16, expected="G"),
                                     character_mock(number=55664, expected="🚀")]
    
    def test_base_character(self):
        for mock in self.base_characters_mock:
            self.assertEqual(base_character(mock.number), mock.expected)

    def test_base_character_raise_base_not_supported(self):
        current_max_base = 55729
        with self.assertRaises(BaseNotSupported):
            base_character(current_max_base)


class TestBase10ToBaseRInt(unittest.TestCase):
    def setUp(self) -> None:
        param_response = namedtuple('MockParamResponse', ['number', 'base', 'result'])
        self.bin_param_response = [param_response(number=0, base=2, result='0'),
                                   param_response(number=1, base=2, result='1'),
                                   param_response(number=2, base=2, result='10'),
                                   param_response(number=7, base=2, result='111'),
                                   param_response(number=8, base=2, result='1000'),
                                   param_response(number=26, base=2, result='11010'),
                                   param_response(number=42, base=2, result='101010'),
                                   param_response(number=1024, base=2, result='10000000000')]
        
        self.octal_param_response = [param_response(number=0, base=8, result='0'),
                                     param_response(number=7, base=8, result='7'),
                                     param_response(number=8, base=8, result='10'),
                                     param_response(number=63, base=8, result='77'),
                                     param_response(number=64, base=8, result='100'),
                                     param_response(number=83, base=8, result='123'),
                                     param_response(number=255, base=8, result='377'),
                                     param_response(number=511, base=8, result='777'),
                                     param_response(number=4096, base=8, result='10000')]
        
        self.hex_param_response = [param_response(number=0, base=16, result='0'),
                                   param_response(number=10, base=16, result='A'),
                                   param_response(number=15, base=16, result='F'),
                                   param_response(number=16, base=16, result='10'),
                                   param_response(number=26, base=16, result='1A'),
                                   param_response(number=31, base=16, result='1F'),
                                   param_response(number=255, base=16, result='FF'),
                                   param_response(number=256, base=16, result='100'),
                                   param_response(number=2748, base=16, result='ABC'),
                                   param_response(number=4095, base=16, result='FFF')]
        
        self.base26_param_response = [param_response(number=0, base=26, result='0'),
                                      param_response(number=10, base=26, result='A'),
                                      param_response(number=25, base=26, result='P'),
                                      param_response(number=26, base=26, result='10'),
                                      param_response(number=36, base=26, result='1A'),
                                      param_response(number=51, base=26, result='1P'),
                                      param_response(number=675, base=26, result='PP'),
                                      param_response(number=676, base=26, result='100'),
                                      param_response(number=7709, base=26, result='BAD'),
                                      param_response(number=17576, base=26, result='1000')]

    def test_base_10_to_bin(self):
        for mock in self.bin_param_response:
            self.assertEqual(base_10_to_r_int(mock.number, mock.base), mock.result)

    def test_base_10_to_octal(self) -> None:
        for mock in self.octal_param_response:
            self.assertEqual(base_10_to_r_int(mock.number, mock.base), mock.result)

    def test_base_10_to_hex(self) -> None:
        for mock in self.hex_param_response:
            self.assertEqual(base_10_to_r_int(mock.number, mock.base), mock.result)

    def test_base_10_to_26(self) -> None:
        for mock in self.base26_param_response:
            self.assertEqual(base_10_to_r_int(mock.number, mock.base), mock.result)     


class TestBase10ToBaseRDecimal(unittest.TestCase):
    def setUp(self) -> None:
        param_response = namedtuple('MockParamResponse', ['number', 'base', 'result'])
        self.bin_param_response = [param_response(number=0.5, base=2, result='1'),
                                   param_response(number=0.25, base=2, result='01'),
                                   param_response(number=0.625, base=2, result='101'),
                                   param_response(number=0.75, base=2, result='11'),
                                   param_response(number=0.8125, base=2, result='1101')]

    def test_base_10_to_bin_decimal(self):
        for mock in self.bin_param_response:
            self.assertEqual(base_10_to_r_dec(mock.number, mock.base), mock.result)


class TestBase10ToBaseR(unittest.TestCase):
    def setUp(self) -> None:
        param_response = namedtuple('MockParamResponse', ['number', 'base', 'result'])
        self.binary_float_param_response = [param_response(number=0.5, base=2, result='0.1'),
                                            param_response(number=0.25, base=2, result='0.01'),
                                            param_response(number=0.625, base=2, result='0.101'),
                                            param_response(number=5.75, base=2, result='101.11'),
                                            param_response(number=10.8125, base=2, result='1010.1101')]

    def test_base_10_to_bin(self):
        for mock in self.binary_float_param_response:
            self.assertEqual(base_10_to_r(mock.number, mock.base), mock.result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
