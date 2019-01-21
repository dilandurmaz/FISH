                        # os ve curses denen iki tane kütüphane projede dahil ediliyor
                        # os kütüphanesi direk olarak termminal konsoluna komut giirmemi sağlıyor. Terminali yeniden boyutlandırma için kullanılıyor
                        # Curses kütüphanesi terminale yazı yazmayı kolaylaştıran bir kütüphane
import os
import curses
import io
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import random
                        # Curses kütüphanesiden yön tuşlarını basıldığını anlamamı sağlayan fonksiyonları
                        # özel olarak dahil ediyorum. Böylece ilerde daha kısa kod yazarak erişebilicem
from random import randint
#import msvcrt as m

class Stack:
     def __init__(self):                        # Sınıfı oluşturan initialize eden kısım
         self.items = []

     def isEmpty(self):                         # Boş mu değil mi ?
         return self.items == []

     def push(self, item):                      # Stackin başına eleman ekler
         self.items.append(item)

     def pop(self):                             # sondan eleman çıkarır
         return self.items.pop(0)

     def peek(self):                            # En tepedeki elemeanı döndürür
         return self.items[len(self.items)-1]

     def size(self):                            # Stackin boyutunu döndürür
         return len(self.items)

     def icindekiler(self):
         return self.items
     def lasitem(self):                         # Stackin son itemini döndürür
         return self.items[0]

# Oyuncunun hareket etmesi sağlanıyor. Yukarı basıldı ise kafanın kordinatları'nın
def oyuncuyubuyut():
    player.insert(0, [player[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                      player[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

os.system('mode con: cols=60 lines=40')
                        # Terminal ekranını boyutlandırma kordinat düzeni (x,y)
curses.initscr()        # Curses kütüphanesinin içindeki başlatıcı fonksiyon.
                        # kütüphaneyi kullanmaya başlamadan önce çağırılması zorunlu
win = curses.newwin(40, 60, 0, 0)
                        # Curses kütüphanesi kendi içinde görünmeyen sanal bir ekrana sahip.
                        # Bu komut ile gerçek terminalimiz ile aynı boyutta bir sanal ekran tanımlıyoruz.
                        # Curses bu sanal ekran yardımı ile çalışan bir kütüphane
win.keypad(1)           # Bazı tuşlar terminalde çeşitli eylemlere sebep oluyor. Keypad değeri 1 olarak ayarlanırsa bu eylemler engelleniyor
                        # Örmeğin yukarı tuşu en son girilen komutu normalde ekrana getirirken artık engellenicek
curses.noecho()         # Normalde bastığınız tuşlar ekranda gözüküyor iken artık gözükmüyor
curses.curs_set(0)      # Yanıp sönen cubuğu imleci gizliyor
win.nodelay(1)          # Tuşa basıldığını anlamamı sağlayan getch fonsiyonu tuşa basılmasa bile bekleme yapmadan çalışıyor
                        # Eğer tuşa basılmadı ise -1 döndürüyor ki ilerde lazım olacak
key = KEY_UP            # Başlangıçta oyuncunun yukarı doğru gitmesini sağlıyor
score = 0
oyuncuboyut = 2
min = 2                 #olışacak balığın boyutları
max = 2


player = [[35, 30], [36, 30]]       # Bu ise oyuncunun kordinatları

balik1stack = Stack()               # Stack objeleri oluşturuluyor şuan boş ilerde dolcak
balik2stack = Stack()
balik3stack = Stack()
balik4stack = Stack()
balik5stack = Stack()               # Milyon tane for yazmak yerini bu liste içinde gezen bir for yazıyorsun misss

listofstack = [balik1stack, balik2stack, balik3stack, balik4stack, balik5stack]


def balikolustur(obj):                         # Balik oluşturur


    for r in range(obj.size()):                # Önce önceki balıktan kalanları temizlediğinden amin olur
        obj.pop
    othersY = [0]                              # Balıklar üst üste gelmesin diye diğer balıkların y koordinatları burda ututlcak
    boyut = randint(min,max)                   # Oluşturulacak balığın boyutu rasgele belirlenir
    eksenY = randint(3,37)                     #Oluşturulacak balığın y koord rasgele belirlenir
    for s in listofstack:                      # Diğer balıkların y kordinatı listeye atılır
        if not s.isEmpty():
            othersY.append(s.lasitem()[0])
        while ((eksenY % 2 == 0) or (eksenY in othersY)):  #Balıkların üst üste gelmemesi ve çift sayılı kordinatlarda olması sağlanır
            eksenY = randint(3, 37)
    for r in range(boyut):
     obj.push([eksenY,r])                      # Değerler balıkStack objesine eklenir. Stackler artık dolu

balikolustur(balik1stack)
balikolustur(balik2stack)
balikolustur(balik3stack)
balikolustur(balik4stack)
balikolustur(balik5stack)

while key != 27:                                                # Esc ye basılmadığı sürece dönen döngü. 27 asii olarak esc demek
    #m.getch()                                                  # kodu Adım adım çalıştırmak için klavye girdisi bekler. Ilk tuş kodu devam ettirir, ikincisi oyuncunun yönünü değiştirir
                                                                # Aktifleştirmek için tagi kaldır

    win.border()                                                # Ekranın kenarlarına çerçeve çiziyor
    #debuglist= []
    #for s in listofstack:
    #    debuglist.append(str(s.lasitem()))
    #    win.addstr(0, 1, 'D'+ str(debuglist) )

    win.addstr(0, 2, 'PUAN : '+ str(score) + "  Boyut: "+ str(oyuncuboyut) )            # Ekranın üstüne puan yazdırıyor
    win.addstr(0, 27, ' Balıklama ')                    # Oyunun ismini tepeye yazıyor
    win.timeout(150)                                    # Oyun hızını ayarlar. Düşük değerler daha hızlıdır. En hızlı sıfır
    prevKey = key                                       # İlerde lazım olacağından en son basılan tuşu ikinci bir değişkende saklıyorum
    event = win.getch()                                 # get.ch yazmak yerine event yazmayı tercih ettiğimden evente atıyorum
    key = key if event == -1 else event                 # Kısa if yazılışı. Eğer getch -1 döndürürse yani tuşa basılmamış ise en son yöne devam ediyor


    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:  # Eğer yön tuşu dışında birşeye basılırsa yada esc geçerli tuş en son basılan geçerli tuşa atanıyor
        key = prevKey



                                                     # Sınırlara ulaşınca balıkların isinlanmasi
    for b in listofstack:
        headofstack = b.peek()                       # Sol sınıra gelince balıklar olacaklar ama hepsi sağa gidiyor yani önemsiz şuan
        if headofstack[1] == 0:
            for r in range(b.size()):
                last = b.pop()
                win.addch(last[0], last[1], ' ')     #Sağ sınıra gelince balık stack'ini boşalt
        if headofstack[1] == 59:
            for r in range(b.size()):
                koord = b.icindekiler()
                win.addch(koord[r][0], koord[r][1], ' ')
            head = b.peek()
            b.push([head[0], 1])
            b.pop()

    die = 0

                                                        # Balıkların hareket etmesi sağlanıyor. Dizinin en başına yeni kafa ekleniyor.
                                                        # Bu sırada boyut 1 artıyor ama ilerde kuruktan bir azaltılarak denge sağlanacak
    for s in listofstack:
     headofstack = s.peek()
     s.push([headofstack[0], headofstack[1] + 1])


    for b in listofstack:
        head = b.peek()
        last = b.pop()                          # Daha önce kafaya yeni bir eleman eklendiğinden boyut artıyordu kuyruktan 1 azaltılarak denge sağlandı
        win.addch(last[0], last[1], ' ')        # Kuyruktan çıkartılan eleman için ekrandaki simge siliniyor
        win.addch(head[0], head[1], '>')        #Eklenen kafa için yeni simge basılıyor ekrana




    for r in range(2):

        # Kenarlara çarparsa oyuncu ölüyor
        if player[0][0] == 0:
            die = 1
            break
        if player[0][1] == 0:
            die = 1
            break
        if player[0][0] == 39:
            die = 1
            break
        if player[0][1] == 59:
            die = 1
            break

        oyuncuyubuyut()

        # oyuncu ekrana çiziliyor
        lastplayer = player.pop()
        win.addch(lastplayer[0], lastplayer[1], ' ')
        win.addch(player[0][0], player[0][1], '#')

        # Oyuncu balığı yediğinde olacaklar
        for b in listofstack:                           # Tüm balıklara bakıyor
            if player[0] in b.icindekiler():            # oyuncunun kafası balıklara çarpmış mı bakıyor
                if b.size() <= oyuncuboyut:             # Oyuncu balıktan küçükmü
                    for r in range(b.size()):           # Balık boyunca tekrar eder
                        last = b.pop()                  # Balık stackini boşaltır
                        win.addch(last[0], last[1], ' ')# Balık ekrandan siliniyor
                    balikolustur(b)                     # Silinen balığın stackini yeni balık ile dolduurr
                    score += 1                          # Puan artıyor
                    if score % 5 == 0:                  # Her 5 puanda boyut artar
                        oyuncuboyut += 1
                        oyuncuyubuyut()
                        max = oyuncuboyut + 1           # Oyuncu büyüyüncce balıklarda büyüyor
                        min = oyuncuboyut-1

                        for b in listofstack:           # Tüm balıklara bakar
                            if b.size() <= oyuncuboyut: # Eğer küçük balık varsa dögü bozulur
                                break
                            elif b.size() <= oyuncuboyut:# Ekranda hiç küçük balık yoksa bir dahaki balığın küçük olması sağlanır
                                min = oyuncuboyut
                                max = oyuncuboyut
                elif b.size() > oyuncuboyut:            # Büyük balığı yersen boğazında kalıyor ölüyon
                    die = 1


    if die == 1: break




curses.endwin()
print("\n---------------------------------------------------------")
print("\n--------------- Oyun bitti puanınız :  " + str(score)+"  --------------- ")
print("\n--------------------------------------------------------- \n")

print("--Yüksek Puanlar-- \n")
# Puan tablosu senden öncekilerin
with io.open("HighScores.txt",'r',encoding='utf8') as f:
    text = f.read()
text += str(score)+"\n"
with io.open("HighScores.txt",'w',encoding='utf8') as f:
    f.write(text)
print(text)
