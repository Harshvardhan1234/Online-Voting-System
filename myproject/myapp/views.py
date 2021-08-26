from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql

def conn():
    import mysql.connector as sql
    from collections import Counter 
    connection=sql.connect(host='localhost',user='root',password='PASSWORD',database="voting")
    candf1=[]
    candf2=[]
    candf3=[]
    no_chof=[]
    dict1={}
    mycursor=connection.cursor()
    mycursor.execute("select * from candidate")
    mydata=mycursor.fetchall()
    for b in mydata:
        candf1.append(b[1])
        candf2.append(b[2])
        candf3.append(b[3])
        no_chof.append(b[4])
    # THE ONLY ONE DICTNERARY______________________________________________________________________________________
    value={"candidate1" :candf1[0], "candidate2" : candf2[0], "candidate3" : candf3[0] ,"no one selected" : no_chof[0]}
    k = Counter(value)#DECENDIG ORDER OF DICTNEARY
    high = k.most_common(4)#success
    extra=[]# for appending the rdered values
    for a in high:
        extra.append(list(a))
    succ={"name":extra[0][0] ,"1score":extra[0][1], "2name":extra[1][0], "2score":extra[1][1], "3name":extra[2][0], "3score":extra[2][1], "4name":extra[3][0] ,"4score":extra[3][1]}
    return succ     

#______________________________________________________________________________________________________________________________________________________________________________________________________

            
def duplicate(request):
    import mysql.connector as sql
    connection=sql.connect(host='localhost',user='root',password='PASSWORD',database="voting")
    candf1=[]
    candf2=[]
    candf3=[]
    no_chof=[]
    dict1={}
    mycursor=connection.cursor()
    mycursor.execute("select * from candidate")
    mydata=mycursor.fetchall()
    for b in mydata:
        candf1.append(b[1])
        candf2.append(b[2])
        candf3.append(b[3])
        no_chof.append(b[4])
    # THE ONLY ONE DICTNERARY______________________________________________________________________________________
    value={"candidate1" :candf1[0], "candidate2" : candf2[0], "candidate3" : candf3[0] ,"no one selected" : no_chof[0]}
    #______________________________________________
    from collections import Counter
    #_______________________________________________
    k = Counter(value)                                        #DECENDIG ORDER OF DICTNEARY
    high = k.most_common(4)                                   #count first 4 value
    extra=[]                                                       # for appending the  values in desc order
    for a in high:
        extra.append(list(a))
    succ={"name":extra[0][0] ,"1score":extra[0][1], "2name":extra[1][0], "2score":extra[1][1], "3name":extra[2][0], "3score":extra[2][1],
          "4name":extra[3][0] ,"4score":extra[3][1]}
    
    # creatig fro dispay as candidate
    
    succ1={"name":extra[0][0] ,succ["name"]:extra[0][1], "2name":extra[1][0],
        succ["2name"]:extra[1][1], "3name":extra[2][0], succ["3name"]:extra[2][1], "4name":extra[3][0] ,succ["4name"]:extra[3][1]}
    flipped = {}                                                                            # to find the dupcleat
    for key, value in succ1.items():                                     # dict_items([('candidate1', [4]), ('candidate2', 4), ('candidate3', 2), ('no one selected', 2)])
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    dict_fro_dup={}
    xyz=succ["1score"]
    
    if len(flipped[xyz]) > 1:
        #print ("yes",flipped[xyz])
        n=0
        for x in flipped[xyz]:
        
            n+=100
            dict_fro_dup["name"+str(n)]=x
        succ.update(dict_fro_dup)
        return HttpResponse(render(request,"resultdup.html",succ))
    else:
        return  HttpResponse(render(request,"thelastpage.html",succ))
    
    
            
#__________________________________________________________________________________________________________________________________________________________________________________________________

#home page
def home(request):
    return render(request,"homepage.html")

#______________________________________________________________________
def adminpass(request):
    return render(request,"adminpass.html")

#______________________________________________________________________
def checkadmin(request):
    num1=request.GET.get("cars")
    num2=request.GET.get("id")
    if num1=="harsh" and num2=="1234":
        return HttpResponse(render(request,"result.html",conn()))
    elif num1=="" and num2=="":
        return HttpResponse(render(request,"empty.html"))
    else:
        return HttpResponse(render(request,"admineerror.html"))

#______________________________________________________________________

def voter(request):
    return render(request,"voterpage.html")


#______________________________________________________________________
def candidate(request):
    import mysql.connector as sql
    connection=sql.connect(host='localhost',user='root',password='PASSWORD',database="voting")
    mycursor=connection.cursor()
    cand1=[]
    cand2=[]
    cand3=[]
    nochoice=[]
    
    mycursor.execute("select * from  candidate")
    mydata=mycursor.fetchall()
    for b in mydata:
        cand1.append(b[1])
        cand2.append(b[2])
        cand3.append(b[3])
        nochoice.append(b[4])

    num1=request.GET.get("candidate")
    if num1=="candidate1":
        num1=cand1[0]+1
        cand1[0]=num1
        num2=cand1[0]
        mycursor.execute("update candidate set cand1="+str(num2)+" where name='ref'")
        connection.commit()
    elif num1=="candidate2":
        num1=cand2[0]+1
        cand2[0]=num1
        num2=cand2[0]
        mycursor.execute("update candidate set cand2="+str(num2)+" where name='ref'")
        connection.commit() 
    elif num1=="candidate3":
        num1=cand3[0]+1
        cand3[0]=num1
        num2=cand3[0]
        mycursor.execute("update candidate set cand3="+str(num2)+" where name='ref'")
        connection.commit()
    else:
        num1=nochoice[0]+1
        nochoice[0]=num1
        num2=nochoice[0]
        mycursor.execute("update candidate set nochoice="+str(num2)+" where name='ref'")
        connection.commit()
    return HttpResponse(render(request,"finalpage.html"))
    
#____________________________________________________________________________________________________________

def mysql(request):
    import mysql.connector as sql
    connection=sql.connect(host='localhost',user='root',password='PASSWORD')
    mycursor=connection.cursor()
    mycursor.execute("create database VOTING")
    table()
    table_security()
    return HttpResponse(render(request,"mysqlconnect.html"))
    
def table():
    import mysql.connector as sql
    connection=sql.connect(host='localhost',user='root',password='PASSWORD',database="VOTING")
    mycursor=connection.cursor()
    mycursor.execute("create table voting_table(USER_NAME char(10),id char(100))")
    mycursor.execute("create table candidate(name char(10),cand1 int(100),cand2 int(100),cand3 int(100),nochoice int(100))")
    mycursor.execute("insert into candidate values('ref',0,0,0,0)")
    connection.commit()
    
def table_security():
    import mysql.connector as sql
    connection=sql.connect(host='localhost',user='root',password='PASSWORD',database="VOTING")
    mycursor=connection.cursor()
    mycursor.execute("create table table_security(the_user_name char(100),user_id char(100))")
    connection.commit()
    
#_____________________________________________________________________________________________________________  
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
def voterdetalis(request):
    import mysql.connector as sql
    connection=sql.connect(host='localhost',user='root',password='PASSWORD',database="VOTING")
    mycursor=connection.cursor()
    name=[]
    ident=[]
    num1=request.GET.get("cars")
    num2=request.GET.get("id")
    #_____________________________________________
   

    #__________________________________________________________________
    namex=[]    # checking duplicate 
    identy=[]
    mycursor.execute("select * from  table_security ")
    mydata=mycursor.fetchall()
    for x in mydata:
        namex.append(x[0])
        identy.append(x[1])
    cars=namex
    cars2=identy



    #________________________________________________________________
    name=[]    # insertion of id 
    ident=[]
    mycursor.execute("select * from  voting_table ")
    mydata=mycursor.fetchall()
    for b in mydata:
        name.append(b[0])
        ident.append(b[1])
    #________________________________________________________________

    if (lsearch(cars,num1)==num1 and lsearch(cars2,num2)==num2):
        return HttpResponse(render(request,"security.html"))

        
    elif (lsearch(name,num1)==num1 and lsearch(ident,num2)==num2):
        our_security=table_security_values_insert(num1,num2)
        our_security1=our_security[0]
        our_security=our_security[1]

        return HttpResponse(render(request,"choicepage.html"))
    
    elif num1=="harsh" and num2=="boss":
        return HttpResponse(render(request,"choicepage.html"))
    else:
        return HttpResponse(render(request,"invalid.html"))
    
   
'''    elif num1=="" and num2=="":
        return HttpResponse(render(request,"emptyvot.html"))
    elif num1==str(num1) and num2=="":
 
        return HttpResponse(render(request,"n_pass_vot.html"))
    
    elif num1=="" and num2==str(num2):
 
        return HttpResponse(render(request,"no_user_vot.html"))    '''
    

#____________________________________________________________________________________________

def table_security_values_insert(num1,num2):
    import mysql.connector as sql
    connection=sql.connect(host='localhost',user='root',password='PASSWORD',database="VOTING")
    mycursor=connection.cursor()
    lis=[]
    sql="insert into table_security values(%s,%s)"
    #===============
    lis.append(num1)
    lis.append(num2)
    #===============
    values=tuple(lis)
    mycursor.execute(sql,values)
    connection.commit()
    #__________________________________________________________________
    mycursor.execute("select * from  table_security ")
    name1=[]    # checking duplicate 
    ident1=[]
    mydata=mycursor.fetchall()
    for x in mydata:
        name1.append(x[0])
        ident1.append(x[1])
    return (name1,ident1)


    



def lsearch(lis,xname):
    for i in lis:
        if i==xname:
            return i
    return False






























