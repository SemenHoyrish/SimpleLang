func text_mult_times
    args
        str s
        int n
    endargs

    def int i
    0
    set i 
    loop

        i < n
        if
            get s
            out
        else
            break
        endif

        i + 1
        set i

    endloop

endfunc


def int a
3
set a


def str text
"Hello\n
set text

>text_mult_times text a


