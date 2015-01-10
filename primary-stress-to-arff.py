#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Date:
	2015/1/7 (last update)
"""

import sys
import os
import codecs
import glob


def usage():
	print "\t" + sys.argv[0], " [DATA_DIR]"
	print "\tFrom a data directory, this script will produce one single weka .arff file."



def main():
	# PARAM: empty string value
	empty = ""

	if len(sys.argv) > 1:
		if not os.path.isdir(sys.argv[1]):
			raise SystemExit, "[ERROR] " + sys.argv[1] + ": directory not found !"
	else:
		print "[ERROR] "+sys.argv[0]+" expected at least 1 argument !"
		usage()
		sys.exit(2)


	res = codecs.open(sys.argv[1] + ".arff", "w", "utf-8")

	res.write("@relation " + sys.argv[1] + "\n")
	res.write("@attribute w-2 {'" + empty + "', 'w0', 'w1', 'w2', 'w3', 'w4'}\n")
	res.write("@attribute w-1 {'" + empty + "', 'w0', 'w1', 'w2', 'w3', 'w4'}\n")
	res.write("@attribute w {'w0', 'w1', 'w2', 'w3', 'w4'}\n")
	res.write("@attribute w+1 {'" + empty + "', 'w0', 'w1', 'w2', 'w3', 'w4'}\n")
	res.write("@attribute w+2 {'" + empty + "', 'w0', 'w1', 'w2', 'w3', 'w4'}\n")
	res.write("@attribute 'Class' {'s0','s2'}\n")
	res.write("@data\n")

	for f in glob.glob(sys.argv[1] + "/*"):

		data = codecs.open(f, "r", "utf-8")
		for line in data.readlines():
			stress = []
			line = line.split(",")

			for i in range(0, len(line[1]), 2):
				stress.append([line[1][i:i+2], line[2][i:i+2].replace("s1", "s0")])


			for i, s in enumerate(stress):
				if i >= 2 :
					res.write("'" + stress[i-2][0] + "',")
				else:
					res.write("'" + empty + "',")
				if i >= 1 :
					res.write("'" + stress[i-1][0] + "',")
				else:
					res.write("'" + empty + "',")

				res.write("'" + s[0] + "',")

				if i + 1 < len(stress):
					res.write("'" + stress[i+1][0] + "',")
				else:
					res.write("'" + empty + "',")
				if i + 2 < len(stress):
					res.write("'" + stress[i+2][0] + "',")
				else:
					res.write("'" + empty + "',")

				res.write("'" + s[1] + "'\n")
		data.close()
	
	print "[DONE] Weka data file generated : " + sys.argv[1] + ".arff"

	

if __name__ == "__main__":
	main()

