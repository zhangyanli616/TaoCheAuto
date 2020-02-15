import unittest
from titan.tt_log import LOG

tt_check = unittest.TestCase()


def assertTrue(expr, msg=None):                    #判断a是否为True
    """Check that the expression is true."""
    tt_check.assertTrue(expr, msg)
    LOG.info("【检查】%s！" % msg)


def assertFalse(expr, msg=None):                 #判断a是否为false
    """Check that the expression is false."""
    tt_check.assertFalse(expr, msg)
    LOG.info("【检查】%s！" % msg)


def assertIs(expr1, expr2, msg=None):            #判断a 与b的对象是否相同，成立则True，否则False
    """Just like self.assertTrue(a is b), but with a nicer default message."""
    """判断a 与b的对象是否相同，成立则True，否则False（注，判断是否同一对象  id(a) 若id相同，则为同一对象）"""
    tt_check.assertIs(expr1, expr2, msg)
    LOG.info("【检查】%s！" % msg)


def assertIsNot(expr1, expr2, msg=None):
    """Just like self.assertTrue(a is not b), but with a nicer default message."""
    """判断a 与b的对象是否相同，不成立True，否则False"""
    tt_check.assertIsNot(expr1, expr2, msg)
    LOG.info("【检查】%s！" % msg)


def assertIsNone(obj, msg=None):
    """Same as self.assertTrue(obj is None), with a nicer default message."""
    """判断obj=None 成立则通过，否则失败"""
    tt_check.assertIsNone(obj, msg)
    LOG.info("【检查】%s，Pass！" % msg)


def assertIsNotNone(obj, msg=None):
    """Included for symmetry with assertIsNone."""
    """判断obj=None 成立则失败，否则通过"""
    tt_check.assertIsNotNone(obj, msg)
    LOG.info("【检查】%s！" % msg)


def assertIsInstance(obj, cls, msg=None):
    """Same as self.assertTrue(isinstance(obj, cls)), with a nicer
            default message."""
    tt_check.assertIsInstance(obj, cls, msg)
    LOG.info("【检查】%s！" % msg)


def assertNotIsInstance(obj, cls, msg=None):
    """Included for symmetry with assertIsInstance."""
    """判断a的数据类型是否为b，isinstance(a,b) 成立则通过，否则失败"""
    tt_check.assertNotIsInstance(obj, cls, msg)
    LOG.info("【检查】%s！" % msg)


def assertIn(member, container, msg=None):
    """Just like self.assertTrue(a in b), but with a nicer default message."""
    """判判断a in b是否成立，正确则True，否则为False"""
    tt_check.assertIn(member, container, msg)
    LOG.info("【检查】%s！" % msg)


def assertNotIn(member, container, msg=None):
    """Just like self.assertTrue(a not in b), but with a nicer default message."""
    """判断a in b是否成立，不成立则True 否则 False"""
    tt_check.assertNotIn(member, container, msg)
    LOG.info("【检查】%s！" % msg)


def assertEqual(first, second, msg=None):
    """Fail if the two objects are unequal as determined by the '=='
               operator.
            """
    """判断fist与second是否一致，msg类似备注，可以为空"""
    tt_check.assertEqual(first, second, msg)
    LOG.info("【检查】%s！" % msg)


def assertNotEqual(first, second, msg=None):
    """Fail if the two objects are equal as determined by the '!='
               operator."""
    """判断fist与second是否不一致，msg类似备注，可以为空"""
    tt_check.assertNotEqual(first, second, msg)
    LOG.info("【检查】%s！" % msg)


def assertAlmostEqual(first, second, places=None, msg=None, delta=None):
    """Fail if the two objects are unequal as determined by their
               difference rounded to the given number of decimal places
               (default 7) and comparing to zero, or by comparing that the
               difference between the two objects is more than the given
               delta.

               Note that decimal places (from zero) are usually not the same
               as significant digits (measured from the most significant digit).

               If the two objects compare equal then they will automatically
               compare almost equal.
            """
    """注：places与delta不能同时存在，否则出异常，
       若a==b，则直接输入正确，不判断下面的过程
       若delta有数，places为空，判断a与b的差的绝对值是否<=delta，满足则正确，否则错误
       若delta为空，places有数，判断b与a的差的绝对值,取小数places位，等于0则正确，否则错误
       若delta为空，places为空，默认赋值places=7"""
    tt_check.assertAlmostEqual(first, second, places, msg, delta)
    LOG.info("【检查】%s！" % msg)


def assertNotAlmostEqual(first, second, places=None, msg=None,
                         delta=None):
    """Fail if the two objects are equal as determined by their
       difference rounded to the given number of decimal places
       (default 7) and comparing to zero, or by comparing that the
       difference between the two objects is less than the given delta.

       Note that decimal places (from zero) are usually not the same
       as significant digits (measured from the most significant digit).

       Objects that are equal automatically fail.
    """
    """同上，但判断相反
       注，delta与places不能同时存在，否则抛出异常"""
    tt_check.assertNotAlmostEqual(first, second, places, msg, delta)
    LOG.info("【检查】%s！" % msg)


def assertCountEqual(first, second, msg=None):
    """An unordered sequence comparison asserting that the same elements,
    regardless of order.  If the same element occurs more than once,
    it verifies that the elements occur the same number of times.

        self.assertEqual(Counter(list(first)),
                         Counter(list(second)))

     Example:
        - [0, 1, 1] and [1, 0, 1] compare equal.
        - [0, 0, 1] and [0, 1] compare unequal.

    """
    """a和b具有相同数字的相同元素，无论它们的顺序如何"""
    tt_check.assertCountEqual(first, second, msg)
    LOG.info("【检查】%s！" % msg)


def assertDictEqual(d1, d2, msg=None):
    """判断字典d1和字典d2是否相等，d1,d2为字典"""
    tt_check.assertDictEqual(d1, d2, msg)
    LOG.info("【检查】%s！" % msg)


def assertListEqual(list1, list2, msg=None):
    """A list-specific equality assertion.

    Args:
        list1: The first list to compare.
        list2: The second list to compare.
        msg: Optional message to use on failure instead of a list of
                differences.
    判断列表list1和列表list2是否相等
    """
    tt_check.assertListEqual(list1, list2, msg)
    LOG.info("【检查】%s！" % msg)


def assertSetEqual(set1, set2, msg=None):
    """A set-specific equality assertion.

    Args:
        set1: The first set to compare.
        set2: The second set to compare.
        msg: Optional message to use on failure instead of a list of
                differences.

    assertSetEqual uses ducktyping to support different types of sets, and
    is optimized for sets specifically (parameters must support a
    difference method).
    """
    tt_check.assertSetEqual(set1, set2, msg)
    LOG.info("【检查】%s！" % msg)


def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None):
    """An equality assertion for ordered sequences (like lists and tuples).

    For the purposes of this function, a valid ordered sequence type is one
    which can be indexed, has a length, and has an equality operator.

    Args:
        seq1: The first sequence to compare.
        seq2: The second sequence to compare.
        seq_type: The expected datatype of the sequences, or None if no
                datatype should be enforced.
        msg: Optional message to use on failure instead of a list of
                differences.
    """
    tt_check.assertSequenceEqual(seq1, seq2, msg, seq_type)
    LOG.info("【检查】%s！" % msg)


def assertTupleEqual(tuple1, tuple2, msg=None):
    """A tuple-specific equality assertion.

     Args:
         tuple1: The first tuple to compare.
         tuple2: The second tuple to compare.
         msg: Optional message to use on failure instead of a list of
                 differences.
     """
    tt_check.assertTupleEqual(tuple1, tuple2, msg)
    LOG.info("【检查】%s！" % msg)


def assertMultiLineEqual(first, second, msg=None):
    """Assert that two multi-line strings are equal."""
    """比较a文本与b文本是否一致，即便多了个换行，也会区分"""
    tt_check.assertMultiLineEqual(first, second, msg)
    LOG.info("【检查】%s！" % msg)


def assertGreater(a, b, msg=None):
    """Just like self.assertTrue(a > b), but with a nicer default message."""
    tt_check.assertGreater(a, b, msg)
    LOG.info("【检查】%s！" % msg)


def assertGreaterEqual(a, b, msg=None):
    """Just like self.assertTrue(a >= b), but with a nicer default message.
    判断a>b 成立则通过，否则失败"""
    tt_check.assertGreaterEqual(a, b, msg)
    LOG.info("【检查】%s！" % msg)


def assertLess(a, b, msg=None):
    """Just like self.assertTrue(a < b), but with a nicer default message.
    判断a<b 成立则通过，否则失败"""
    tt_check.assertLess(a, b, msg)
    LOG.info("【检查】%s！" % msg)


def assertLessEqual(a, b, msg=None):
    """Just like self.assertTrue(a <= b), but with a nicer default message.
    判断a<=b 成立则通过，否则失败"""
    tt_check.assertLessEqual(a, b, msg)
    LOG.info("【检查:%s！" % msg)


def assertRegex(text, expected_regex, msg=None):
    """Fail the test unless the text matches the regular expression.
    除非文本与正则表达式匹配，否则测试失败"""
    tt_check.assertRegex(text, expected_regex, msg)
    LOG.info("【检查】%s！" % msg)


def assertNotRegex(text, unexpected_regex, msg=None):
    """Fail the test if the text matches the regular expression.
    如果文本与正则表达式匹配，则测试失败"""
    tt_check.assertNotRegex(text, unexpected_regex, msg)
    LOG.info("【检查】%s！" % msg)
