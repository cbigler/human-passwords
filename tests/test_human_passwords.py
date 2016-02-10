#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_human-passwords
----------------------------------

Tests for `human-passwords` module.
"""

import unittest

from human_passwords import human_passwords
import human_passwords.dictionary.en


class TestHumanPasswords(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_default_lang_is_en(self):
        password = human_passwords.generate()
        self.assertEqual(len(password), 17)
        self.assertTrue(password[:4] in human_passwords.dictionary.en.d[4])
        num = int(password[4:8])
        self.assertTrue(password[8:13] in human_passwords.dictionary.en.d[5])
        num = int(password[13])

    def test_generate_en(self):
        password = human_passwords.generate('en')
        self.assertEqual(len(password), 17)
        self.assertTrue(password[:4] in human_passwords.dictionary.en.d[4])
        num = int(password[4:8])
        self.assertTrue(password[8:13] in human_passwords.dictionary.en.d[5])
        num = int(password[13])

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
