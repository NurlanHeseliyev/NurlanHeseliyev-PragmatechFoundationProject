 # 2 ed sozlerin ardicil yazilmasi

from os import add_dll_directory


a="salam"
b= "dunya"
c=a+b
print(c)
 # eyni sozu 5 defe ardicil yazilmasi
a = "SalamDunya"
print (a *5)


print ("fuzzy\ncoffee\n") #bu setir sozlerin alt alta yigimidir
print ("19","07","1997",sep= "/") #bu setir dogum tarixidir


#hesablama usullari
print ("{}+{}={}". format (2,3,2+3)) 
print (10-7) 
print (4+1)  
print (3*1)  
print (10//4)
print (10%4)   
print (10/4)  

# "*" deyerini 1,2,3,4 edelerini ardicil cap eldilmesidi
a=5
b=6
c= a+4*b
print (c)

print( "*" * 1)
print( "*" * 2)
print( "*" * 3)
print( "*" * 4)


# "SalamDunya" szoundeki herifleri alt-alta cap edilmesidi
a= "SalamDunya"
b=(1,2,3,4,5,)
print (a[0])
print (a[1])
print (a[2])
print (a[3])
print (a[4])
print (len(a))
print (len(b))
print (a[len(a)-4])
print (b[len(b)-4]) 
print (a[-5:])
print (a[:5])
print (a[5:])
print (a[0:5:])
print (a[0:5:2])

 #dogum tarixi
GUn=input("gun")
Ay=input("ay")
IL=input("IL")
print ("Dogum Tarix",GUn,Ay,IL)
 
#ededlerin hesablanmasi
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print("Toplama",a+b+c)

#edeelrin siralanmasi
a=input("a:")
b=input("b:")
c=input("c:")
print("Toplama",a+b+c)
#(0-55) geder cap edilir 
for say in range (0,56,2):
    print(say)
    #(0-56) araligda olan cut edeleri cap edir
for say in range (0,56):
    print(say)

# eyer yas 18 den kicikdirse yas sehfdi eyer 18 den coxdursa yas duzgun cap edilib bildirilir
yas = int(input("yasiniza daxil olun:"))
if yas <18:
 print ("daxil olunan yas sehfdir")
else: 
 print("yasiniz 18-di")
 
#qiymetlendirme
qiymetlendirme = int(input("qiymeti daxil edin"))
if qiymetlendirme ==  5:
    print ("sizin qiymetiniz 5`i")
elif qiymetlendirme == 4:
    print("sizin qiymetiniz 4`i")
elif qiymetlendirme == 3:
        print("sizin qiymetiniz 3`i")

elif qiymetlendirme == 2:
        print("sizin qiymetiniz 2`i")
else:
 print("secim yanlisdi") 
# yazilan kodda True ve folse beli xeyir  olarag cap olumur
# true cap edir
a="Ne qeder"
b= "Sert olsa dalgalar"
c=  "Qayalara cirpinib" 
d=  "geri doner"
e= "Mubariz Tagiyev"
if a=="Ne qeder" and b=="Sert olsa dalgalar"and c=="Qayalara cirpinib" and d== "geri doner"  and e == "Mubariz Tagiyev": 
    print("beli")
else: print("xeyir")
#folse cap edir
a="Ne qeder"
b= "Sert olsa dalgalar"
c=  "Qayalara cirpinib" 
d=  "geri doner"
e= "Mubariz Tagiyev"
if a=="Sert olsa dalgalar" or b=="Ne qeder"or c=="geri doner" or d== "Qayalara cirpinib"  or e == "Salam Dunya": 
    print("beli")
else: print("xeyir")

#0dan-15 geder olan cut edeleri ekrana cap edir
a=0
while a<15:
    print("Sira Sayi:",a)
    a=a+2
#  1 den  556 ya geder  olan cut edeleri ardicil vurularag cap edilir 
a=1
while a<556:
    print("Sira Sayi:",a)  
    a*= 2 


#  
for say in range (0,56,2):
    print(say)
for say in range (0,56):
    print(say) 

#funksiyalar 
def MubarizTagiyev () :
 print("Ne geder")
print("Sert olsa dalgalar")
print("Qayalara cirpinib ")
print("Geri doner")
MubarizTagiyev ()
    
def Mubariz (Tagiyev):
 print("Ne geder",Tagiyev)
Mubariz ("Sert olsa dalgalar")
def Mubariz (Tagiyev):
 print("Qayalara cirpinib",Tagiyev)
Mubariz("Geri doner")
print("Mubariz Tagiyev")

def MubarizTagiyev ():
    print("Ne geder")
print("Sert olsa dalgalar")
print("Qayalara cirpinib ")
print("Geri doner")
MubarizTagiyev () 

