func hello
    args
        int n
    endargs

    def int i
    loop
        i < n
        if
            "Hello"
            outn
        else
            break
        endif
        i + 1
        set i
    endloop
endfunc
