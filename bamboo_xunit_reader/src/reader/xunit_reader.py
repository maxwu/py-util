#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'


import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class XunitReader:
    def __init__(self, xmlfile = None):
        self.tc_num = 0
        self.res = {}
        if xmlfile is not None:
            self.scan(xmlfile)

    def scan(self, xmlfile):
        if xmlfile is None:
            return
        tree = ET.ElementTree(file=xmlfile)
        for elem in tree.iter(tag='testcase'):
            classname = elem.get('classname')
            if classname.startswith('Rf Regression.'):
                classname = classname[14:]
            tcname =  classname + '.' + elem.get('name')
            passed = True
            for child in elem:
                if 'failure' == child.tag:
                    passed = False

            if passed:
                if tcname not in self.res:
                    self.res[tcname] = {'pass': 1, 'failure': 0}
                    self.tc_num += 1
                else:
                    self.res[tcname]['pass'] += 1
            else:
                if tcname not in self.res:
                    self.res[tcname] = {'pass': 0, 'failure': 1}
                    self.tc_num += 1
                else:
                    self.res[tcname]['failure'] += 1

            self.res[tcname]['passrate'] = (self.res[tcname]['pass'] + 0.0)/(self.res[tcname]['failure'] + self.res[tcname]['pass'])
        print "XML %s scanned and total %d cases merged." % (xmlfile, self.tc_num)

    def get_tc_num(self):
        return self.tc_num

    def get_failed_tc(self):
        return [tcname for tcname in self.res if self.res[tcname]['failure'] > 0]

    def get_sorted_by_passrate(self):
        return sorted(self.res.items(), key=lambda d: d[1]['passrate'], reverse=True)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('At least one Unit File is requested.')

    if 'unittest.main' in sys.modules.keys():
        print "XunitReader under UT"

    xreader = XunitReader()

    for arg in sys.argv[1:]:
        print "processing %s" %(arg)
        xreader.scan(arg)
    for k, v  in xreader.get_sorted_by_passrate():
        print "TCname=%s, times=%d, Passrate=%f" %(k, v['pass']+v['failure'], v['passrate'])
    pass
