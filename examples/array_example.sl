def arr->str langs

"Python"
add langs

"C++"
add langs

"Java"
add langs


def int langs.len()
len langs
set langs.len()

def int i
loop
	i < langs.len()
	if
		get i
		read langs
		outn
	else
		break
	endif
	i + 1
	set i 
endloop
