#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 08:11:22 2021

@author: florian
"""

import pandas as pd
import Levenshtein


df = pd.read_csv('20210103_hundenamen.csv')
L_dist = df['HUNDENAME'].apply(lambda x: Levenshtein.distance(x, 'Luca'))
names = df['HUNDENAME'][L_dist==1].unique()
for elem in names:
    print(elem, end=',')