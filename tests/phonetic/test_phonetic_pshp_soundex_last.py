# -*- coding: utf-8 -*-

# Copyright 2014-2018 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.phonetic.test_phonetic_pshp_soundex_last.

This module contains unit tests for abydos.phonetic.PSHPSoundexLast
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.phonetic import PSHPSoundexLast, pshp_soundex_last


class PSHPSoundexLastTestCases(unittest.TestCase):
    """Test PSHP Soundex functions.

    test cases for abydos.phonetic.PSHPSoundexLast
    """

    pa = PSHPSoundexLast()

    def test_pshp_soundex_last(self):
        """Test abydos.phonetic.PSHPSoundexLast."""
        # Base case
        self.assertEqual(self.pa.encode(''), '0000')

        self.assertEqual(self.pa.encode('JAMES'), 'J500')
        self.assertEqual(self.pa.encode('JOHN'), 'J500')
        self.assertEqual(self.pa.encode('PAT'), 'P300')
        self.assertEqual(self.pa.encode('PETER'), 'P350')

        self.assertEqual(self.pa.encode('Smith'), 'S530')
        self.assertEqual(self.pa.encode('van Damme'), 'D500')
        self.assertEqual(self.pa.encode('MacNeil'), 'M400')
        self.assertEqual(self.pa.encode('McNeil'), 'M400')
        self.assertEqual(self.pa.encode('Edwards'), 'A353')
        self.assertEqual(self.pa.encode('Gin'), 'J500')
        self.assertEqual(self.pa.encode('Cillian'), 'S450')
        self.assertEqual(self.pa.encode('Christopher'), 'K523')
        self.assertEqual(self.pa.encode('Carme'), 'K500')
        self.assertEqual(self.pa.encode('Knight'), 'N230')
        self.assertEqual(self.pa.encode('Phillip'), 'F410')
        self.assertEqual(self.pa.encode('Wein'), 'V500')
        self.assertEqual(self.pa.encode('Wagner', german=True), 'V255')
        self.assertEqual(self.pa.encode('Pence'), 'P500')
        self.assertEqual(self.pa.encode('Less'), 'L000')
        self.assertEqual(self.pa.encode('Simpson'), 'S525')
        self.assertEqual(self.pa.encode('Samson'), 'S250')
        self.assertEqual(self.pa.encode('Lang'), 'L500')
        self.assertEqual(self.pa.encode('Hagan'), 'H500')
        self.assertEqual(self.pa.encode('Cartes', german=True), 'K500')
        self.assertEqual(self.pa.encode('Kats', german=True), 'K000')
        self.assertEqual(self.pa.encode('Schultze', german=True), 'S400')
        self.assertEqual(self.pa.encode('Alze', german=True), 'A400')
        self.assertEqual(self.pa.encode('Galz', german=True), 'G400')
        self.assertEqual(self.pa.encode('Alte', german=True), 'A400')
        self.assertEqual(self.pa.encode('Alte', max_length=-1), 'A43')
        self.assertEqual(self.pa.encode('Altemaier', max_length=-1), 'A4355')

        # Test wrapper
        self.assertEqual(pshp_soundex_last('Smith'), 'S530')


if __name__ == '__main__':
    unittest.main()
