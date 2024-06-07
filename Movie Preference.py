class Film:
    def __init__(self, ad, puan, oyuncular):
        self.ad = ad
        self.puan = puan
        self.oyuncular = oyuncular

    def __repr__(self):
        return f"{self.ad} - Puan: {self.puan}"

def film_ekle():
    ad = input("Film adı: ")
    puan = float(input("Film puanı: "))
    oyuncular = input("Filmdeki oyuncuları virgülle ayırarak girin: ").split(',')
    return Film(ad, puan, oyuncular)

def filmleri_sirala(filmler):
    return sorted(filmler, key=lambda x: x.puan, reverse=True)

def main():
    filmler = []
    film_sayisi = int(input("Kaç film gireceksiniz? "))

    for _ in range(film_sayisi):
        film = film_ekle()
        filmler.append(film)

    siralanmis_filmler = filmleri_sirala(filmler)
    print("\nFilmler puanlarına göre sıralandı:")
    for film in siralanmis_filmler:
        print(film)

if __name__ == "__main__":
    main()
