include stdlib

def arr->str words
def int words.len

"Apple"
add words
"Tree"
add words
"Juice"
add words
"Wolf"
add words

len words
set words.len
words.len - 1
set words.len


def int players_count

"Enter players count: "
out
in players_count

def int i

def str word

>random 0 words.len
read words
set word

def int player
>random 1 players_count
set player

func wait
    args
        str message
    endargs
    get message
    out
    in s_
endfunc


>clear

loop
    i < players_count
    if
        "Player number "
        out
        i + 1
        outn
        >wait "Press Enter to see who are you!"
        i + 1 == player
        if
            "SPY!"
            outn
        else
            "Word is: "
            out
            get word
            outn
        endif
        >wait "Press Enter to clear"
        >clear
    else
        break
    endif
    i + 1
    set i
endloop


>wait "Press Enter to get answer"
"Word is: "
out
get word
outn
"Spy is player number "
out
get player
outn
