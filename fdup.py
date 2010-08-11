#!/usr/bin/env python

# fdup - A program to find duplicated files
# Copyright (C) 2010 Roland Kammerer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import hashlib

def inodesort(a, b):
    return int(os.stat(a).st_ino - os.stat(b).st_ino)

if len(sys.argv) != 1:
    print sys.argv[0], ":"
    print "read files from stdin"
    sys.exit(1)

K = (1024)
M = (K * K)

d = dict()

fnames = [ fname.rstrip() for fname in sys.stdin.readlines() ]
if not fnames: sys.exit(1)

fnames = sorted(fnames, inodesort)

for fname in fnames:
    try:
        fp = open(fname, 'r')
    except IOError as (errno, strerror):
        print >> sys.stderr, "I/O error({0}): {1} ({2})".format(errno, strerror, fname)
        continue
    key = fp.read(1*K)
    fp.close()

    key += str(os.stat(fname).st_size)
    if not d.has_key(key):
        d[key] = list()
    d[key].append(fname)

for fnames in d:
    if len(d[fnames]) == 1: continue
    hashes = dict()
    for fname in d[fnames]:
        #m = hashlib.sha1()
        m = hashlib.md5()
        fp = open(fname, 'r')
        while True:
            content = fp.read(5*M)
            if content: m.update(content)
            else: break
        fp.close()
        digest = m.digest()
        if not hashes.has_key(digest):
            hashes[digest] = list()
        hashes[digest].append(fname)

    for digest in hashes:
        if len(hashes[digest]) > 1:
            for fname in hashes[digest]:
                print fname
            print 
