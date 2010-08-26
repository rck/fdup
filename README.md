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

`$ find $PWD -type f > files.txt
$ ./fdup.py < files.txt`

RESULTS
=======
Testdirectory is my $HOME which contained 62022 files. 
There are 18680 duplicate files (empty files, duplicates from svn and git repos)

<table>
   <tr>
      <th>Program</th><th>user</th><th>system</th><th>cpu (%)</th><th>**total**</th>
   </tr>
   <tr>
      <td>fdup<td><td>3.38s</td><td>6.10s</td><td>5</td><td>**3:01.89**<td>
   </tr>
   <tr>
      <td>fslint<td><td>18.04s</td><td>9.20s</td><td>12</td><td>3:41.20<td>
   </tr>
   <tr>
      <td>fdupes<td><td>62.35s</td><td>15.46s</td><td>20</td><td>6:16.49<td>
   </tr>
   <tr>
      <td>duff<td><td>22.59s</td><td>4.42s</td><td>6</td><td>7:18.13<td>
   </tr>
   <tr>
      <td>dupseek<td><td>18.33s</td><td>6.55s</td><td>4</td><td>8:30.35<td>
   </tr>
   <tr>
      <td>ftwin<td><td>15.94s</td><td>7.50s</td><td>3</td><td>9:57.91<td>
   </tr>
</table>
