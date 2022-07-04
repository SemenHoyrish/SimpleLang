def str s_
def str s__
def str s___

def int i_
def int i__
def int i___

def bool b_
def bool b__
def bool b___

func out_str_array
    args
        arr->str arr
    endargs
    def int i
    0
    set i

    def int l
    len arr
    set l

    loop
        i < l
        if
            "["
            out
            get i
            out
            "] -> "
            out
            get i
            read arr
            outn
        else
            break
        endif
        i + 1
        set i
    endloop
endfunc

func out_int_array
    args
        arr->int arr
    endargs
    def int i
    0
    set i

    def int l
    len arr
    set l

    loop
        i < l
        if
            "["
            out
            get i
            out
            "] -> "
            out
            get i
            read arr
            outn
        else
            break
        endif
        i + 1
        set i
    endloop
endfunc

func out_bool_array
    args
        arr->int arr
    endargs
    def int i
    0
    set i

    def int l
    len arr
    set l

    loop
        i < l
        if
            "["
            out
            get i
            out
            "] -> "
            out
            get i
            read arr
            outn
        else
            break
        endif
        i + 1
        set i
    endloop
endfunc

func concat_str_arrays
    args
        arr->str arr
        arr->str arr_
    endargs

    def int i
    0
    set i

    def int l
    len arr_
    set l

    loop
        i < l
        if
           get i
           read arr_
           add arr
        else
            break
        endif
        i + 1
        set i
    endloop

    get arr
    return
endfunc

func concat_int_arrays
    args
        arr->int arr
        arr->int arr_
    endargs

    def int i
    0
    set i

    def int l
    len arr_
    set l

    loop
        i < l
        if
           get i
           read arr_
           add arr
        else
            break
        endif
        i + 1
        set i
    endloop

    get arr
    return
endfunc

func concat_bool_arrays
    args
        arr->bool arr
        arr->bool arr_
    endargs

    def int i
    0
    set i

    def int l
    len arr_
    set l

    loop
        i < l
        if
           get i
           read arr_
           add arr
        else
            break
        endif
        i + 1
        set i
    endloop

    get arr
    return
endfunc

func concat_strs
    args
        str s
        str s_
    endargs

    def arr->str arr
    def arr->str arr_

    get s
    strtoarr
    set arr

    get s_
    strtoarr
    set arr_

    >concat_str_arrays arr arr_
    arrtostr
    return
endfunc

