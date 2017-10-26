#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json

filenames = os.listdir('../files')

post = []
for filename in filenames:
    if os.path.isfile(filename):
        with open(("../files/"+filename), 'r') as file:
            post.append(json.loads(file.read()))

print(post)

print(os.path.isfile("a.c"))
