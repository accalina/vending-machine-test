
class VendingMachine:

    def __init__(self):
        """ Initialisasi variable yang dipakai """
        self.pricelist = {
            "Cokelat" : 15000,
            "Tango" : 12000,
            "Oreo" : 10000,
            "Chips" : 8000,
            "Biskuit" : 6000,
        }
        self.fractions = [
            2000, 
            5000, 
            10000, 
            20000, 
            50000
        ]
        self.shopingCart = {}
        self.cash = 0

    def checkCash(self, cash):
        """ Mengecek pecahan dan nilai cash yang diberikan """
        statusCheck = False
        if cash > 0 :
            for fraction in self.fractions:
                if cash % fraction == 0:
                    statusCheck = True
                    self.cash = cash
        return statusCheck


    def calculate(self, cash):
        """ Menghitung sisa kembalian dan barang yang dibeli """
        if self.checkCash(cash):
            for keyname in self.pricelist.keys():
                while self.cash >= self.pricelist[keyname]:
                    self.cash -= self.pricelist[keyname]
                    self.assignBucket(keyname)
            self.displayResult()
            # print(self.shopingCart)
            # print(self.cash)
        else:
            print("Pecahan uang tidak valid, pastikan pecahan uang sebesar (2000, 5000, 10000, 20000, 50000)")

    def displayResult(self):
        """ Menampilkan hasil sisa kembalian dan barang yang dibeli """
        print(f"Sisa kembalian: {self.cash}")
        print("Barang yang dibeli:")
        for index, item in enumerate(self.shopingCart.keys()):
            print(f"{index + 1}. {self.shopingCart[item]} buah {item}")

    def assignBucket(self, keyname):
        """ Memberi nilai kepada variable shopping cart (keranjang belanja) """
        if keyname in self.shopingCart:
            self.shopingCart[keyname] += 1
        else:
            self.shopingCart[keyname] = 1


if __name__ == "__main__":
    v = VendingMachine()
    cashinput = int(input("Masukan jumlah uang: "))
    v.calculate(cashinput)

