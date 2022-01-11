def average(array):
    toplam= sum(set(array))
    adet = len(set(array))
    sonuc = toplam/adet
    return sonuc
