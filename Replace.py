def censor (text,word):
    #text = text.lower()
    word = word.lower()
    rep_str = ''
    for c in word: rep_str += '*' 
    ret = text.replace(word,rep_str)
    print ret
    return ret
censor('sssdffe', 'f')
