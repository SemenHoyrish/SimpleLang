func sum
	args
		int a
		int b
	endargs

	a + b
	return
endfunc

func mult
	args
		int a
		int b
	endargs

	a * b
	return
endfunc

def int a
def int b

"Enter first number: 
out
in a
"Enter second number: 
out
in b

"Sum is: 
out
>sum a b
out
"\nMult is "
out
>mult a b
out
"\n
out
