#istifadeciler qeydiyatdan kecir 
# qeydiyatdan kecen istifadeciye biz rutbe veririk 
# daxil olan istifadecinin rutbesine gore mesaj gonderirik

#from login import b
import USER.register
import USER.login
import USER

#file connection/ fayl baglantisi
myfile = open("sample.txt","rt")
data=myfile.read()
print(data)
 
#fayla melumat yazmag
myfile = open("sample.txt","a")
myfile. write(" Bir kere yukselen bayrak bir daha enmez. Mehmet Emin Resulzade")