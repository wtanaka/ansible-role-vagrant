#!/usr/bin/env python
# coding=utf-8
# Copyright (C) 2016 Wesley Tanaka
"""
"""

import yaml

if __name__ == "__main__":
  with open('RedHat.yml', 'rb') as fp:
    print yaml.load(fp.read())
