
CypherText = "NRUWJXXNAJ BTWP GZY YMJ HFJXFW HNUMJW NX STY XJHZWJ JSTZLM KTW HQFXXNKNJI YWFSXRNXXNTSX YMJ WJFQ RJXXFLJ NX NSHQZIJI GJQTB FSI BFX JSHWDUYJI ZXNSL F ANLSJWJ HNUMJW BNYM PJDBTWI MFHPFYMTS VZZI PGPWAZL AWNQ YXKEFNT NQ ZHL OQHHXGRBWP YLT MCQ BK QSJGDNFBGZ SVI YFQ VGAQLHY RTBFS JCTW"
frequencies = {}

for char in CypherText:
    if char in sorted(frequencies):
        frequencies[char] += 1
    else:
        frequencies[char] = 1

for word, value in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
    print(word, value, sep=" | ")

print(CypherText.replace('J','E').replace('N','T').replace('W','A').replace('X','O'))
