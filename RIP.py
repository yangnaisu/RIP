#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

#import packages
import re
import os
import sys
import subprocess
import argparse
from collections import defaultdict



def check_software_availability(softwares):
    green_tick = '\033[92m\u2713\033[0m'  # 绿色对勾符号
    red_cross = '\033[91m\u2717\033[0m'  # 红色叉号符号
    for software in softwares:
        try:
            p = subprocess.run(f'command -v {software}',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                shell=True
            )
            print(f"{green_tick} {software.ljust(10)}\tPATH:{p.stdout.decode('utf-8')}", end='')
        except subprocess.CalledProcessError as e:
            print(f"{red_cross} {software.ljust(10)}\t未安装或不可用,请检查！")
            return False
    return True


def parse_args():
    parse = argparse.ArgumentParser(description='识别逆转座子多态')  
    parse.add_argument('-r', '--ref', default=2, type=int, metavar='', required=True, help='Radius of Cylinder') 
    parse.add_argument('-s', '--step', default=2, type=int, metavar='', help='处理步骤') 
    parse.add_argument('-t', '--threads', default=1, type=int, metavar='', help='number of threads [1]') 
    parse.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parse.parse_args()  # 4、解析参数对象获得解析对象
    return args

def ref_in():
	pass

def main():
	"""
	The main-function:
	"""

	try:
		# Help needed?

		if '-d' in sys.argv:
			sys.stdout.write(__description__)
			sys.exit()

		if '-h' in sys.argv or '-help' in sys.argv:
			sys.stdout.write(__usage__ % options)
			sys.exit()

		if '-v' in sys.argv:
			sys.stdout.write(__version__ % (__version_no__, __version_date__))
			sys.exit()

		# Under which mode should sine_finder run?

		if len(sys.argv) == 1: 
			print('hello')
			
	except Exception as e:
		# catch unrecognized errors and write pythons error message to
		# STDERR
		sys.stderr.write("%s\n" % e)

if __name__ == '__main__':

    #检查必要软件
    software_to_check = ["bwa", "bwa-mem2", "samtools", "bedtools1"]  # 需要检查的软件列表
    print('检查软件依赖')
    if check_software_availability(software_to_check):
        print("软件检测完成！")
    else:
        print("依赖软件缺失，请检查！")

    args = parse_args()
    main() 