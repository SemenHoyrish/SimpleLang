def int NUM
4
set NUM

func test
	args
		str s
		bool new_line
	endargs
	def int i
	loop
		i < NUM
		if
			get s
			out
			get new_line
			if
				"\n"
				out
			else
			endif
		else
			break
		endif
		i + 1
		set i
	endloop

endfunc


>test "Hello@@ " true
