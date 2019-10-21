# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:06:36 2019

@author: pelan
"""
from roots import *


def test_quadroots():
    assert quad_roots(1.0, 1.0, -12.0) == ((3+0j), (-4+0j))

test_quadroots()

import sys
def test_quadroots_types():
    try:
        quad_roots("", "green", "hi")
    except:
        assert(sys.exc_info()[0] == TypeError)

test_quadroots_types()

def test_quadroots_zerocoeff():
    try:
        quad_roots(a=0.0)
    except:
        assert(sys.exc_info()[0] == ValueError)

test_quadroots_zerocoeff()
