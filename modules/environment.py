#!/usr/bin/env python
# coding:utf-8
# author:Leslie Binbin

import os


def run(**args):
    print '[*] in environment module.'
    return str(os.environ)
