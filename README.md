# BTXT (Boolean Text)

BTXT is a a half-programming language that uses three symbols separated by commas: !,&, and |.
It also uses keys that can change the formatting of the output and push comments or commands.

to run BTXT you will need to have python3.7 installed.
You will use the command line to run btxt.

BTXT files have .btxt as the extension.

If using linux with BTXT, edit the ~/.bash_aliases file and insert the following code:
If you do not have a ~/.bash_aliases file, you need to make one.
```shell
btxt = { echo "$1" > .tmp_btxt && python3 [LOCATION OF booltext.py]; }
```

This is a sample btxt file:
```btxt
&,&,&,&,&,&,&,&
!,!,&,&,|,|
<COLOR>
ORANGE
<DELAY>
<RESET>
<SEPARATOR>
, 
```

This is the output:
```text
and, and, and, and, and, and, and, and
not, not, and, and, or, or
```
It is orange and delays in between each line. 
The screen clears before the output shows.
The words are separated by ', '
