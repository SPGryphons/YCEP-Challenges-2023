First, set two breakspoints at the two compare instructions in start()
```
pwndbg> b *0x00005555555554fb
Breakpoint 1 at 0x5555555554fb
pwndbg> b *0x0000555555555503
Breakpoint 2 at 0x555555555503
```
Run the program, and enter some values <br>
When it hits the breakpoint, check the stack values, we get this.
```
pwndbg> x/20d $rsp
0x7fffffffdf60: 28      0       10      10
0x7fffffffdf70: 2021662414      0       1959009735      0
0x7fffffffdf80: 0       0       -90     -77
0x7fffffffdf90: 1684500940      0       1684500936      0
0x7fffffffdfa0: -8256   32767   1431655873      21845
pwndbg>
```
the values are at -0x14 and -0x18 from RBP. RBP=`0x7fffffffdfa0`. this gives `0x7ffffffdf8c`(-77) and `0x7ffffffdf88`(-90)
this means the coordinates are -77,-90
