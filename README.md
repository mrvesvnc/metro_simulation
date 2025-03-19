# metro_simulation
Bu proje, bir metro ağında iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı bulan bir simülasyon sunar.
Projede kullanılan algoritmalar sayesinde en az aktarmayla veya en kısa sürede gidilebilecek yollar hesaplanır.

collections - deque yapısı kullanılarak BFS algoritması için kuyruk yapısı oluşturulmuştur.
heapq - A* algoritması için öncelik kuyruğu oluşturmak amacıyla kullanılmıştır.
pandas - Test sonuçlarının tablo formatında gösterilmesi için kullanılmıştır.
ace_tools - Test sonuçlarını görüntülemek için özel olarak eklenmiştir.


## BFS Algoritması (En Az Aktarma)

Genişlik Öncelikli Arama (Breadth-First Search - BFS) kullanılarak en az aktarma gerektiren rota bulunur. BFS, bir kuyruğa istasyonları ekleyerek en kısa bağlantılı yolları keşfeder.

Başlangıç istasyonu kuyruğa eklenir.

Kuyruk boşalana kadar işlemler devam eder:

İlk eleman kuyruğun başından çıkarılır.

Eğer hedef istasyon bulunursa, yol döndürülür.

Ziyaret edilmemiş komşu istasyonlar kuyruğa eklenir.

Eğer hedefe ulaşılamazsa None döndürülür.

## A* Algoritması (En Hızlı Rota)

A* algoritması kullanılarak en kısa sürede ulaşılabilecek rota hesaplanır.
A* algoritması, öncelik kuyruğunu kullanarak en kısa sürede ulaşılan yolu belirler.

Başlangıç istasyonu öncelik kuyruğuna eklenir.

Kuyruk boşalana kadar işlemler devam eder:

Süresi en az olan istasyon kuyruğun başından çıkarılır.

Eğer hedef istasyon bulunursa, yol ve toplam süre döndürülür.

Komşu istasyonlar ve süreleri kuyruğa eklenir.

Eğer hedefe ulaşılamazsa None döndürülür.

Neden BFS ve A* Algoritmaları Kullanıldı?

BFS → En az aktarmalı rota bulmak için en iyi yöntemdir.

A* → En kısa süreli rotayı bulmak için öncelik sıralaması yapmamıza olanak tanır.

## Örnek Kullanım ve Test Sonuçları

AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

Keçiören'den AŞTİ'ye:
En az aktarmalı rota: Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (19 dakika): Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

Kızılay'dan Gar'a:
En az aktarmalı rota: Kızılay -> Sıhhiye -> Gar
En hızlı rota (9 dakika): Kızılay -> Sıhhiye -> Gar

Sıhhiye'den Demetevler'e:
En az aktarmalı rota: Sıhhiye -> Gar -> Demetevler
En hızlı rota (15 dakika): Sıhhiye -> Gar -> Demetevler

## Projeyi Geliştirme Fikirleri

Metro haritası üzerinde görselleştirme yapılabilir.

Aktarma istasyonlarında ek süre eklenerek daha gerçekçi hesaplama yapılabilir.

Metro ağı daha büyük bir şehir simülasyonuyla genişletilebilir.

Gerçek dünya verisiyle test edilerek analizler yapılabilir.

