#!/usr/bin/env python
# coding:utf-8
# author:Leslie Binbin

import os


def run(**args):
    print '[*] In dirlister module.'
    files = os.listdir('.')
    return str(files)
