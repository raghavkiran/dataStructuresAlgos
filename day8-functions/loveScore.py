def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    tCount=0
    rCount=0
    uCount=0
    eCount=0
    for c in combined_name:
        if c=='T' or c=='t':
            tCount+=1
        if c=='R' or c=='r':
            rCount+=1
        if c=='U' or c=='u':
            uCount+=1
        if c=='E' or c=='e':
            eCount+=1
    
    trueCount = tCount + rCount + uCount + eCount
    print(tCount, rCount, uCount, eCount)
    print(trueCount)

    lCount=0
    oCount=0
    vCount=0
    eCount=0
    for c in combined_name:
        if c=='L' or c=='l':
            lCount+=1
        if c=='O' or c=='o':
            oCount+=1
        if c=='V' or c=='v':
            vCount+=1
        if c=='E' or c=='e':
            eCount+=1
    
    loveCount = lCount + oCount + vCount + eCount
    print(lCount, oCount, vCount,  eCount)
    print(loveCount)
    
    print(f"{trueCount}{loveCount}")
    
    
#calculate_love_score("Kanye West", "Kim Kardashian")
#calculate_love_score("Kiran", "Pavithra")

calculate_love_score("Raghavendra", "Pavithra")

