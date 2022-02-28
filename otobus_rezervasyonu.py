import sys

class otobus():
    
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True
        
        self.koltuk1 = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
        self.koltuk2 = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
        
    
    
    def program(self):
        secim = self.Menu()
        
        
        if secim == 1:
            self.Rezervasyon()
        
        elif secim == 2:
            self.Butun_koltuklar()
        
        elif secim == 3:
            self.Bos_koltuklar()
        
        elif secim == 4:
            self.Dolu_koltuklar()
        
        elif secim == 5:
            self.Rezervasyon_ıptalı()
        
        elif secim == 6:
            print("Çıkılıyor...")
            sys.exit()
    
    
    def Menu(self):
        secim = int(input("----- Şehirler arası otobüsümüze hoş geldiniz -----\n\n1-)Rezervasyon yap\n2-)Bütün Koltukları göster\n3-)Boş Koltukları göster\n4-)Dolu koltukları göster\n5-)rezervasyon iptali\n6-)Çıkış\n\nSeçim yap: "))
    
        while secim < 1 or secim > 6:
            secim = int(input("Lütfen belirtilen seçeneklerden birini giriniz: "))
        return secim


    def Rezervasyon(self):
        self.adi = input("Adinizi giriniz: ")
        self.soyadi = input("Soyadinizi giriniz: ")
        self.cinsiyeti = input("Cinsiyetinizi giriniz(E/K): ")
        self.kisi = self.adi+" "+self.soyadi+","+self.cinsiyeti  
        
        
        self.koltukNo = input("Koltuk numaranızı giriniz(a1-b1-c1/a3-b3-c3): ")
        
        
        if not(self.koltukNo in self.koltuk1):
            self.koltukNo = input("Orası dolu lütfen başka bir yer seçiniz: ")
        

        self.indexi = self.koltuk1.index(self.koltukNo)
        
        self.koltuk1[self.indexi] = self.kisi+","+self.koltukNo      
        
        
    def Butun_koltuklar(self):
        print("\t\t↓ Bütün Koltuklarımız ↓")
        print(self.koltuk2)
    
    
    def Bos_koltuklar(self):
        
        for i in range(8):
            if len(self.koltuk1[i]) == 2:
                print(self.koltuk1[i])
    
    
    def Dolu_koltuklar(self):
        
        for j in range(8):
            
            if len(self.koltuk1[j]) != 2:
                print(self.koltuk1[j])

    
    def Rezervasyon_ıptalı(self):
        
        self.rezerv = input("Koltuk numaranızı giriniz: ")
        
        self.index = self.koltuk2.index(self.rezerv)
        
        
        if self.koltuk1[self.index] != 2:
            self.koltuk1[self.index] = self.koltuk2[self.index]
        
        else:
            return ("Orası dolu bir koltuk")
                    
baslat = otobus("Kamilkoç") 

while baslat.calisma:
    baslat.program()



