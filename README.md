Description
===========
*fdup.py* is a simple and fast program that finds duplicate files.

Why?
----
Because it is amazingly fast. Much faster than fdupes, which is written in C and
much more readable than fslint/findup.

Python is not a limiting factor, but disc speed is. Therefore a sane algorithm
to find/sort out potential duplicate files is much more important than the
language used. In the end its all about the algorithm and disc performance.
Fstat, disc IO, hashing is in Python nearly as fast as in C, don't worry.

Usage
=====
`$ find $PWD -type f | ./fdup.py`

or to exclude the time *find* needs:

`$ find $PWD -type f > files.txt`
`$ cat files.txt | ./fdup.py`
