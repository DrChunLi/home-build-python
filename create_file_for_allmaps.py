#! /bin/env python
import sys
import pandas as pd

blastout = sys.argv[1]         # the blast out file
genetic_map = sys.argv[2]      # the genetic map file

with open(blastout) as _in:
	blast_lines = _in.readlines()

with open(genetic_map) as _in2:
	gtmap_lines = _in2.readlines()

# create a dict for blast_lines
blastDict = {}
for line in blast_lines:
	_ls = line.split("\t")
	# dict[qseid] = [sseqid, qstart qend, sstart send] 
	blastDict[_ls[0]] = [_ls[1], int(_ls[6]), int(_ls[7]), int(_ls[8]), int(_ls[9])]


# deal lines in genetic map
"""
markerID	shortID	position
hua_TRINITY_DN153231_c1_g2_905	0
hua_TRINITY_DN133981_c2_g4_992	0.827
"""
for _line in gtmap_lines:
	markerID, chrom, cMpos = _line.strip().split("\t")
	contigID = "_".join(markerID.split("_")[0:-1])
	contigPos = int(markerID.split("_")[-1])
	assert contigPos>0
	if contigID in blastDict:
		_sseqid, _qstart, _qend, _sstart, _send = blastDict[contigID]
		if _sstart < _send:                                       # on the + strand
			newPos = contigPos - _qstart + _sstart
			# 62 230 = 989933776 989933608, by say 102, newPos = 102-62+989933776
		else:
			newPos = _sstart - (contigPos - _qstart)              # on the - strand
		print(markerID + "\t" + chrom + "\t" + cMpos + "\t" + _sseqid + "\t" + str(_qstart) + "\t" + str(_qend) + "\t" + str(_sstart) + "\t" + str(_send) + "\t" + str(newPos))




