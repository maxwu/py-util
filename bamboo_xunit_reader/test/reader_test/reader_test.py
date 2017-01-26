#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'


import unittest
from reader.xunit_reader import XunitReader


class TestXunitReader_188(unittest.TestCase):
    def setUp(self):
        self.xreader = XunitReader('./test/test_data/XCI-188-xunit.xml')

    def tearDown(self):
        self.xreader = None
        pass

    def test_all_tc_number(self):
        self.assertEqual(self.xreader.get_tc_num(), 17)

    def test_all_failed_tc(self):
        self.assertEqual(len(self.xreader.get_failed_tc()), 2, 'Length of failure TC list')
        self.assertListEqual([
                                'Trafficgen.Dhcp.wait_untial_all_dhcp_session_negotiated',
                                'Trafficgen.Dhcp.ixia_dhcp_v4_with_single_tag',
                             ],
                             self.xreader.get_failed_tc())

    def test_sorted_by_passrate_first_15(self):
        for k, v in self.xreader.get_sorted_by_passrate()[:15]:
            self.assertEqual(v['passrate'], 1.0)

    def test_sorted_by_passrate_last_2(self):
        for k, v in self.xreader.get_sorted_by_passrate()[-2:]:
            self.assertEqual(v['passrate'], 0)


class TestXunitReader_188_plus_187(unittest.TestCase):
    def setUp(self):
        self.xreader = XunitReader()
        self.xreader.scan('./test/test_data/XCI-188-xunit.xml')
        self.xreader.scan('./test/test_data/XCI-187-xunit.xml')

    def tearDown(self):
        self.xreader = None
        pass

    def test_all_tc_number(self):
        self.assertEqual(self.xreader.get_tc_num(), 283)

    def test_all_failed_tc(self):
        self.assertIn('Trafficgen.Dhcp.wait_untial_all_dhcp_session_negotiated',
                      self.xreader.get_failed_tc(),
                      'This is a failed case')


if __name__ == '__main__':
    unittest.main()
