from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

    def __lt__(self, other: 'Istasyon'):
        return self.idx < other.idx

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[str]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        queue = deque([(baslangic, [baslangic.ad])])
        ziyaret_edilenler = set()

        while queue:
            mevcut, yol = queue.popleft()
            
            if mevcut == hedef:
                return yol
            
            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edilenler:
                    ziyaret_edilenler.add(komsu.idx)
                    yeni_yol = yol + [komsu.ad] if komsu.ad != mevcut.ad else yol
                    queue.append((komsu, yeni_yol))
        
        return None  # Yol bulunamazsa

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[str], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        oncelik_kuyrugu = [(0, baslangic, [baslangic.ad])]
        ziyaret_edilenler = {}

        while oncelik_kuyrugu:
            mevcut_sure, mevcut, yol = heapq.heappop(oncelik_kuyrugu)
            
            if mevcut == hedef:
                return yol, mevcut_sure
            
            if mevcut.idx in ziyaret_edilenler and ziyaret_edilenler[mevcut.idx] <= mevcut_sure:
                continue
            
            ziyaret_edilenler[mevcut.idx] = mevcut_sure
            
            for komsu, sure in mevcut.komsular:
                yeni_yol = yol + [komsu.ad] if komsu.ad != mevcut.ad else yol
                heapq.heappush(oncelik_kuyrugu, (mevcut_sure + sure, komsu, yeni_yol))
        
        return None  # Yol bulunamazsa

# Test Senaryoları
if __name__ == "__main__":
    metro = MetroAgi()
    
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)
    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)
    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)
    
    test_senaryolari = [
        ("M1", "K4", "AŞTİ'den OSB'ye"),
        ("T1", "T4", "Batıkent'ten Keçiören'e"),
        ("T4", "M1", "Keçiören'den AŞTİ'ye"),
        ("K1", "M4", "Kızılay'dan Gar'a"),
        ("M3", "T2", "Sıhhiye'den Demetevler'e")
    ]
    
    print("\n=== Test Senaryoları ===")
    for baslangic, hedef, aciklama in test_senaryolari:
        print(f"\n{aciklama}:")
        rota = metro.en_az_aktarma_bul(baslangic, hedef)
        if rota:
            print("En az aktarmalı rota:", " -> ".join(rota))
        else:
            print("Rota bulunamadı!")
        
        sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))
        else:
            print("En hızlı rota bulunamadı!")
