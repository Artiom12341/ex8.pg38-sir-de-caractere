"""	 REZOLVĂ! Elaboraţi un program care citeşte de la tastatură şirul de caractere
S şi afişează pe ecran:
a)	 numărul de apariţii ale caracterului ’A’ în şirul X;
b) şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’;
c) şirul obţinut prin radierea din şirul X a tuturor apariţiilor caracterului ’B’;
d)	 numărul de apariţii ale silabei MA în şirul X;
e) şirul obţinut prin substituirea tuturor apariţiilor în şirul X a silabei MA prin
silaba TA;
f) şirul obţinut prin radierea din şirul X a tuturor apariţiilor silabei TO;
g)	 scrierea inversă a şirului X;"""
x=str(input("Sirul de caractere-"))
print("a)numărul de apariţii ale caracterului ’A’ în şirul x=",x.count('A'))
s1=''
if 'A' in x:
    for i in range(0,len(x)):
        if x[i]=='A':
            s1=x.replace('A','*')
    print("b)şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’=",s1)
else:
    print("b)şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’=",x)
s2=''
if 'B' in x:
    for i in range(0,len(x)):
        if x[i]=='B':
            s2=x.replace('B','')
    print("c)şirul obţinut prin radierea din şirul X a tuturor apariţiilor caracterului ’B’=",s2)
else:
    print("c)şirul obţinut prin radierea din şirul X a tuturor apariţiilor caracterului ’B’=",x)
print("d)numărul de apariţii ale silabei 'MA' în şirul X=",x.count('MA'))
s3=''
if 'MA' in x:
    for i in range(0,len(x)):
        if ((x[i]=='M') and (x[i+1]=='A')):
            s3=x.replace('MA','TA')   
    print("e)şirul obţinut prin substituirea tuturor apariţiilor în şirul X a silabei MA prin silaba TA=",s3)
else:
    print("e)şirul obţinut prin substituirea tuturor apariţiilor în şirul X a silabei MA prinsilaba TA=",x)
s4=''
if 'TO' in x:
    for i in range(0,len(x)):
        if ((x[i]=='T') and (x[i+1]=='O')):
            s4=x.replace('TO','')
    print("f)şirul obţinut prin radierea din şirul X a tuturor apariţiilor silabei TO=",s4)
else:
    print("f)şirul obţinut prin radierea din şirul X a tuturor apariţiilor silabei TO=",x)
print("g)scrierea inversă a şirului X=",x[::-1])



