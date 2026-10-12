# -*- coding: utf-8 -*-
"""Configuration pytest : garantit que la racine du projet est importable."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
