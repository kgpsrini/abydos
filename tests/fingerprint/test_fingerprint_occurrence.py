# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
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

"""abydos.tests.fingerprint.test_fingerprint_occurrence.

This module contains unit tests for abydos.fingerprint.Occurrence
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.fingerprint import Occurrence, occurrence_fingerprint


class OccurrenceFingerprintTestCases(unittest.TestCase):
    """Test Cisłak & Grabowski's occurrence fingerprint functions.

    abydos.fingerprint.Occurrence
    """

    fp = Occurrence()

    def test_occurrence_fingerprint(self):
        """Test abydos.fingerprint.Occurrence."""
        # Base case
        self.assertEqual(self.fp.fingerprint(''), 0)

        # https://arxiv.org/pdf/1711.08475.pdf
        self.assertEqual(self.fp.fingerprint('instance'), 0b1110111000010000)

        self.assertEqual(self.fp.fingerprint('inst'), 0b0100111000000000)
        self.assertEqual(
            self.fp.fingerprint('instance', 15), 0b111011100001000
        )
        self.assertEqual(
            self.fp.fingerprint('instance', 32),
            0b11101110000100000000000000000000,
        )
        self.assertEqual(
            self.fp.fingerprint('instance', 64),
            0b11101110000100000000000000000000 << 32,
        )

        # Test wrapper
        self.assertEqual(
            occurrence_fingerprint('instance', 32),
            0b11101110000100000000000000000000,
        )


if __name__ == '__main__':
    unittest.main()
