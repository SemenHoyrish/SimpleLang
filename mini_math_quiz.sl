def str name
"Enter your name: 
out
in name

def int answ
def int count

"Enter a result of 5 + 1: 
out
in answ
answ == 6
if
count + 1
set count
else
endif


"Enter a result of 6 / 2: 
out
in answ
answ == 3
if
    count + 1
    set count
else
endif

"Enter a square of 9: 
out
in answ
answ == 9 * 9 
if
    count + 1
    set count
else
endif


"You gave 
out
get count
out
" right answers\n
out
"And you gave 
out
3 - count
out
" wrong answers\n
out

count == 3
if
    "Congratulations, 
    out
    get name
    out
    "!!!\n"
    out
else
endif
