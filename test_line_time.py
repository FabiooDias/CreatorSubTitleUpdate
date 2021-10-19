from Control.classCalculeTime import Calculator_time
import re

def test_format_time():
    test = Calculator_time()
    test_argument = ['00:00:04,059', '00:00:06,650']
    test_argument1 = 1.0
    expected = '00:00:05,059 --> 00:00:07,650\n'
    actual = test.line_time_update(test_argument, test_argument1)
    message = f'line_time_update([00:00:04,059, 00:00:06,650]) precisa retorna um tempo no formato esperado mais esta retornando {actual}'
    assert actual == expected, message