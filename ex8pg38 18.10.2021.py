s1='AVXCD FGH ERZAZA'
s2=''
s3=''
s4=''
for i in range(0,len(s1)):
    s2=s1.replace(s1[i],chr(ord(s1[i])+1))
    for i in range(0,len(s2)):
        if s2[i]=='Z':
            s3=s2.replace('Z','A')
            for i in range(0,len(s3)):
                if s3[i]==' ':
                    s4=s3.replace(' ','-')
print(s4)
