# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zIlt646QeCLwZIHWp88Fi6-C-nbaEX-r
"""


from roboflow import Roboflow
rf = Roboflow(api_key="5TcRlkOaNxVB0VVKZPDJ")
project = rf.workspace("leukemia").project("leukemia-2.0")
dataset = project.version(2).download("tfrecord")
