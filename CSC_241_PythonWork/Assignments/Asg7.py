Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: J:\School\Autumn 2016-17\CSC 241\Mod 7\asg7template.py ======
RUNNING CHECK ...
unique([[0,1,1,0],[1,1,0],[0,0,1,0]]): PASSED!
unique([[1,2,3,4],[5,6],[7,8,9,10,11,12]]): PASSED!
unique([[1,2,3,1,5],[2,1,3],[5,5,2,1,3]]): PASSED!

vote([[1,0],[0,0],[0,0]],['Smith','Jones']): FAILED!
Traceback (most recent call last):
  File "J:\School\Autumn 2016-17\CSC 241\Mod 7\asg7template.py", line 55, in <module>
    print("vote([[1,0],[0,100],[0,0]],['Smith','Jones']): " + check(vote([[1,0],[0,100],[0,0]],['Smith','Jones']),'The winner is Jones with 100 votes.'))
  File "J:\School\Autumn 2016-17\CSC 241\Mod 7\asg7template.py", line 37, in vote
    anw = 'The winner is {} with {} votes.'.format(namelst[i],tot[i])
IndexError: list index out of range
>>> 
====== RESTART: J:\School\Autumn 2016-17\CSC 241\Mod 7\asg7template.py ======
RUNNING CHECK ...
unique([[0,1,1,0],[1,1,0],[0,0,1,0]]): PASSED!
unique([[1,2,3,4],[5,6],[7,8,9,10,11,12]]): PASSED!
unique([[1,2,3,1,5],[2,1,3],[5,5,2,1,3]]): PASSED!

Traceback (most recent call last):
  File "J:\School\Autumn 2016-17\CSC 241\Mod 7\asg7template.py", line 54, in <module>
    print("vote([[1,0],[0,0],[0,0]],['Smith','Jones']): " + check(vote([[1,0],[0,0],[0,0]],['Smith','Jones']),'The winner is Smith with 1 votes.'))
  File "J:\School\Autumn 2016-17\CSC 241\Mod 7\asg7template.py", line 35, in vote
    for i in range(tot):
TypeError: 'list' object cannot be interpreted as an integer
>>> 
====== RESTART: J:\School\Autumn 2016-17\CSC 241\Mod 7\asg7template.py ======
RUNNING CHECK ...
unique([[0,1,1,0],[1,1,0],[0,0,1,0]]): PASSED!
unique([[1,2,3,4],[5,6],[7,8,9,10,11,12]]): PASSED!
unique([[1,2,3,1,5],[2,1,3],[5,5,2,1,3]]): PASSED!

vote([[1,0],[0,0],[0,0]],['Smith','Jones']): PASSED!
vote([[1,0],[0,100],[0,0]],['Smith','Jones']): PASSED!
vote([[1,0,3],[0,10,1],[0,0,16]],['Smith','Jones','Williams']): PASSED!

>>> 
