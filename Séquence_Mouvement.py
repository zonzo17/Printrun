#!/usr/bin/python
import sys
import os
import inspect
import re
import unittest
import atexit

# Add relative pygcode to path
from testutils import add_pygcode_to_path, str_lines
add_pygcode_to_path()

# Units under test
from pygcode import gcodes
from pygcode import words
from pygcode import machine

from pygcode.exceptions import GCodeWordStrError 

atexit.register(lambda: input("\nPress Enter to exit."))

print('          YOOOOO WHATS UP CRONUS !!!           ')

#import serial
import time
from printrun.printcore import printcore

p = printcore('COM5', 115200)

class MachineGCodeProcessingTests(unittest.TestCase):
    def assert_processed_lines(self, line_data, machine):
        """
        Process lines & assert machine's position
        :param line_data: list of tuples [('g1 x2', {'X':2}), ... ]
        """
        for (i, (line_str, expected_pos)) in enumerate(line_data):
            line = Line(line_str)
            if line.block:
                machine.process_block(line.block)
            # Assert possition change correct
            if expected_pos is not None:
                p1 = machine.pos
                p2 = machine.Position(**expected_pos)
                self.assertEqual(p1, p2, "index:%i '%s': %r != %r" % (i, line_str, p1, p2))

    # Rapid Movement
    def test_rapid_abs(self):
        m = Machine()
        m.process_gcodes(GCodeAbsoluteDistanceMode())
        line_data = [
            ('', {}),  # start @ 0,0,0
            ('g0 x0 y10',       {'X':0, 'Y':10}),
            ('   x10 y10',      {'X':10, 'Y':10}),
            ('   x10 y0',       {'X':10, 'Y':0}),
            ('   x0 y0',        {'X':0, 'Y':0}),
        ]
        self.assert_processed_lines(line_data, m)
p.send(line_data)