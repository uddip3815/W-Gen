print('''
            WW                    WW            GG            EEEEEEEE      NN     NNNN
             WW        WW        WW           GG              EE            NN    NN NN
              WW     WW  WW     WW          GG    GGGGGG      EEEEE         NN   NN  NN
               WW   WW    WW   WW            GG   GG  GG      EE            NN  NN   NN
                WWWW       WWWW               GGGG     GG     EEEEEEEE      NNNN     NN     
                                                                                            v 1.0
''')
print ('''       
                            <===[[ By uddip3815 ]]===>                                 
''')
print (" ")
print (" ")

length=int(input("Enter the number of characters: "))
print (" ")
li_name=input("Name your wordlist: ")
print (" ")
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print (" ")
print ("Generating Wordlist Please Wait!")
print (" ")
print ("   <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>   ")
print (" ")
lista=[0 for x in range(length)]
x=length-1
string="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
list_of_results=[]
file1=open(li_name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in range (length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in range(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in range(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
print ("Completed Generating Wordlist")
print (" ")
print ("   >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<   ")
print (" ")
print ("Please check "+str(li_name)+" in your W-Gen directoy")
print (" ")
print ("   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ")
