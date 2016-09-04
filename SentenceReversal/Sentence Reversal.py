def rev_word(s):
    s = s.strip();
    l = s.split()
    l.reverse()
    s = ' '.join(l)
    
    return(s)

rev_word('Hi John,   are you ready to go?')
