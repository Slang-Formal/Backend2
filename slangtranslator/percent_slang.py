from slangtranslator.slang_words import slang_word

  

def slang_ratio(s):
    gather =[]
    words = s.split()
    for x in words:
        gather.append(x)
    count = len(gather)
    slang_words = slang_word(s)
    count2 = len(slang_words)
    percent = count2/count
    percent = percent*100
    percent = int(percent)
    percent = str(percent) + '%'
    return percent
