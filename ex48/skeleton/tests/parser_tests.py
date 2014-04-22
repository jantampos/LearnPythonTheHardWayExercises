from nose.tools import *
from ex48 import parser
from ex48 import lexicon

def _test_words(input):
  words = lexicon.scan(input)
  test = parser.Parser(words)
  return test

def test_parse_object():
  assert_equal(_test_words("the bear").parse_object(), ("noun", "princess"))
  assert_equal(_test_words("the princess").parse_object(), ("noun", "princess"))
  assert_equal(_test_words("the north").parse_object(), ("direction", "north"))
  assert_raises(ParserError, _test_words, "will fail")


