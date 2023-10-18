text=""

for j in range(1, 34+1):
    for i in range(1, 68+1):
        if j==1 and ((i==20 or i==24) or (28<=i and i<=30) or (34<=i and i<=37) or (41<=i and i<=44) or (i==48 or i==52)):
            text += "*"
        elif j==2 and ((i==20 or i==24) or (i==27 or i==31) or (i==34 or i==38) or (i==41 or i==45) or (i==48 or i==52)):
            text += "*"
        elif j==3 and ((i==20 or i==24) or (i==27 or i==31) or (i==34 or i==38) or (i==41 or i==45) or (i==49 or i==51)):
            text += "*"
        elif j==4 and ((20<=i and i<=24) or (27<=i and i<=31) or (34<=i and i<=37) or (41<=i and i<=44) or i==50):
            text += "*"
        elif j==5 and ((i==20 or i==24) or (i==27 or i==31) or i==34 or i==41 or i==50):
            text += "*"
        elif j==6 and ((i==20 or i==24) or (i==27 or i==31) or i==34 or i==41 or i==50):
            text += "*"
        elif j==7 and ((i==20 or i==24) or (i==27 or i==31) or i==34 or i==41 or i==50):
            text += "*"
        elif j==8 and (i==0):
            text += "*"
        elif j==9 and (i==0):
            text += "*"
        elif j==10 and ():
            text += "*"
        elif j==11 and ():
            text += "*"
        elif j==12 and ():
            text += "*"
        elif j==13 and ():
            text += "*"
        elif j==14 and ():
            text += "*"
        elif j==15 and ():
            text += "*"
        elif j==16 and ():
            text += "*"
        elif j==17 and (i==0):
            text += "*"
        elif j==18 and (i==0):
            text += "*"
        elif j==19 and ((i==20 or i==24)  or (28<=i and i<=30) or (i==34 or i==38)):
            text += "*"
        elif j==20 and ((i==20 or i==24)  or (i==27 or i==31) or (i==34 or i==38)):
            text += "*"
        elif j==21 and ((i==20 or i==24)  or (i==27 or i==31)):
            text += "*"
        elif j==22 and ((i==20 or i==24)  or (i==27 or i==31) or i==36):
            text += "*"
        elif j==23 and ((i==20 or i==22 or i==24)  or (i==27 or i==31) or (i==34 or i==38)):
            text += "*"
        elif j==24 and ((i==20 or i==22 or i==24)  or (i==27 or i==31) or (i==34 or i==38)):
            text += "*"
        elif j==25 and ((i==21 or i==23)  or (28<=i and i<=30) or (i==34 or i==38)):
            text += "*"
        elif j==26 and (i==0):
            text += "*"
        elif j==27 and (i==0):
            text += "*"
        elif j==28 and ((30<=i and i<=33) or (38<=i and i<=40) or (i==44 or i==48)):
            text += "*"
        elif j==29 and ((i==30 or i==34) or (i==37 or i==41) or (i==44 or i==48)):
            text += "*"
        elif j==30 and ((i==30 or i==34) or (i==37 or i==41) or (i==45 or i==47)):
            text += "*"
        elif j==31 and ((i==30 or i==34) or (37<=i and i<=41) or i==46):
            text += "*"
        elif j==32 and ((i==30 or i==34) or (i==37 or i==41) or i==46):
            text += "*"
        elif j==33 and ((i==30 or i==34) or (i==37 or i==41) or i==46):
            text += "*"
        elif j==34 and ((30<=i and i<=33) or (i==37 or i==41) or i==46):
            text += "*"
        else:
            text += " "
            
    text += "\n"


print(text)
