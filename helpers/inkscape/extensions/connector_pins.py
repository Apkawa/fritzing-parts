#!/usr/bin/env python
#-*- coding: utf-8 -*-

import inkex
from inkex.extensions import EffectExtension

class MyExtensionName(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument('-s', '--start', action='store', type=int, dest='start',
                                     default=1, help='Start numeration')
        self.arg_parser.add_argument('-r', '--reverse', action='store', dest='reverse',
                                     type=inkex.Boolean, default=False, help='Reverse')

    def effect(self):
        option = self.options
        self._main_function(option)


    def _main_function(self, option):
        selection = sorted(self.selected.values(), key=lambda e: sum(e.bounding_box().center), reverse=option.reverse)
        for i, e in enumerate(selection, start=option.start):
            e.set('id', 'connector%spin' % i)


if __name__ == '__main__':
    MyExtension = MyExtensionName()
    MyExtension.affect()
