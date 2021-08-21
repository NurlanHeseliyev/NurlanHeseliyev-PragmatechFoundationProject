#oop
class QeydiyyatdanKeç:
    def __init__(self,Ad,Soyad,Email,Username,Password):
        self.Ad=Ad
        self.Soyad=Soyad
        self.Email=Email
        self.Username=Username
        self.Password=Password
    def TelebOlunanMelumatlar(self):
        print("Ad:",self.Ad)
        print("Soyad:",self.Soyad)
        print("Email:",self.Email)
        print("Username:",self.Username)
        print("Password:",self.Password)
QeyatdanKeç=QeydiyyatdanKeç("Məmməd Əmin Axund Hacı",
"Rəsulzadə","MəhəmmədRəsulzade1884@mail.com",
"Rəsulzade Molla Ələkbər oğlu ","31/01/1884")
QeyatdanKeç.TelebOlunanMelumatlar()

class Car:
 def __init__(self,brand,model,buraxlisIli,qiymet): 
     self.brand=brand
     self.model=model
     self.buraxlisIli=buraxlisIli
     self.qiymet=qiymet
     

Car_1=Car("VAZ",2107,2012,6999.99)
Car_2=Car("VAZ", 2107.20008,4999.99)

print(Car-2)
print(Car_2.brand)

