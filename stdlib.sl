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


func reverse_str_array
    args
        arr->str array
    endargs
    
    def arr->str result
    def int array.len
    len array
    set array.len
    array.len - 1
    set array.len

    def int i
    loop
        i < array.len + 1
        if
            array.len - i
            read array
            add result
        else
            break
        endif
        i + 1
        set i
    endloop
    get result
    return
endfunc

func reverse_int_array
    args
        arr->int array
    endargs
    
    def arr->int result
    def int array.len
    len array
    set array.len
    array.len - 1
    set array.len

    def int i
    loop
        i < array.len + 1
        if
            array.len - i
            read array
            add result
        else
            break
        endif
        i + 1
        set i
    endloop
    get result
    return
endfunc

func reverse_bool_array
    args
        arr->bool array
    endargs
    
    def arr->bool result
    def int array.len
    len array
    set array.len
    array.len - 1
    set array.len

    def int i
    loop
        i < array.len + 1
        if
            array.len - i
            read array
            add result
        else
            break
        endif
        i + 1
        set i
    endloop
    get result
    return
endfunc

func random
    args
        int min
        int max
    endargs
    $RANDOM min max
    return
endfunc

func clear
    args
    endargs
    $CLEAR
endfunc

func error
    args
        str message
    endargs
    $ERROR
endfunc

func pow
    args
        int num
        int pow
    endargs
    def int i
    def int result
    1
    set result
    loop
        i < pow
        if
            result * num
            set result
        else
            break
        endif
        i + 1
        set i
    endloop
    get result
    return
endfunc

func str_to_int
    args
        str string
    endargs

    def arr->str symbols
    def int symbols.len
    get string
    strtoarr
    set symbols
    len symbols
    set symbols.len

    def int result

    def str s
    def int n
    def int k
    def int i
    loop
        i < symbols.len
        if
            10
            set n
            get i
            read symbols
            set s
            s == "1"
            if
                1
                set n
            else   
            endif
            s == "2"
            if
                2
                set n
            else
            endif
            s == "3"
            if
                3
                set n
            else
            endif
            s == "4"
            if
                4
                set n
            else
            endif
            s == "5"
            if
                5
                set n
            else
            endif
            s == "6"
            if
                6
                set n
            else
            endif
            s == "7"
            if
                7
                set n
            else
            endif
            s == "8"
            if
                8
                set n
            else
            endif
            s == "9"
            if
                9
                set n
            else
            endif
            s == "0"
            if
                0
                set n
            else
            endif

            n == 10
            if
                >concat_strs "string: '" string
                set s_
                >concat_strs s_ "' cannot be converted to int!"
                set s_
                >error s_
                0
                set result
                break
            else
                symbols.len - i - 1
                set k

                >pow 10 k
                set k 

                result + n * k
                set result
            endif        
        else
            break
        endif
        i + 1
        set i
    endloop

    get result
    return
endfunc


func int_to_str
    args
        int integer
    endargs
    def arr->str digits

    def int n
    loop
        integer > 0
        if
            integer % 10
            set n
            n == 1
            if
                "1"
                add digits
            else   
            endif
            n == 2
            if
                "2"
                add digits
            else
            endif
            n == 3
            if
                "3"
                add digits
            else
            endif
            n == 4
            if
                "4"
                add digits
            else
            endif
            n == 5
            if
                "5"
                add digits
            else
            endif
            n == 6
            if
                "6"
                add digits
            else
            endif
            n == 7
            if
                "7"
                add digits
            else
            endif
            n == 8
            if
                "8"
                add digits
            else
            endif
            n == 9
            if
                "9"
                add digits
            else
            endif
            n == 0
            if
                "0"
                add digits
            else
            endif

            integer / 10
            set integer
        else
            break
        endif
    endloop

    >reverse_str_array digits
    arrtostr
    
    return
endfunc


func bool_to_int
    args
        bool boolean
    endargs
   
    get boolean
    if
        1
    else
        0
    endif
    return
endfunc

func bool_to_str
    args
        bool boolean
    endargs
   
    get boolean
    if
        "true"
    else
        "false
    endif
    return
endfunc
