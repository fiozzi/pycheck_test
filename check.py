# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:25:10 2022

@author: fabrizio
"""

import importlib
import sys
import os
import argparse
import math

#wrap inside try block, this code must not generate error
sub_dir = 'uploads'
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

def check(cond):
    if eval(cond):
        return True
    else:
        return False

try:
    m = importlib.import_module(args.filename, package=sub_dir)
    max_score = 0
    current_score = 0

	#########################
	###### START TESTS ######
	#########################

    param_list = [ 
        [(3,4), 0.75, 1],
        [(4,4), 1., 1],
        [(0,4), 0., 1],
        [(3,0), None, 2],
        [(1,4), 0.25, 1]
    ]
    for test_param in param_list:
        max_score += test_param[2]
        try:
            if isinstance(test_param[1],(int, float)):
                if check('math.isclose(m.division(*test_param[0]), test_param[1])'):
                    current_score += test_param[2]
                    print(f'Passed! {current_score}/{max_score}')
            else:
                if m.division(*test_param[0]) is None:
                    current_score += test_param[2]
                    print(f'Passed! {current_score}/{max_score}')
        except ZeroDivisionError:
            print(f'Not Passed! {current_score}/{max_score}')
	
	#########################
	###### END TESTS ######
	#########################
	
    print(f'Score: {current_score}/{max_score}')
    final_score = round(100*current_score/max_score,0)
    sys.exit(final_score)
	
except Exception as e:
	print('Test file returned early due to exception')
	print(str(e))
	sys.exit(0)
