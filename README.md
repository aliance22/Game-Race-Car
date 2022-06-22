# Game Development Life Cycle (GDLC)

## -GAME RACE CAR-

1. Initiation
   <p> Game yang kami buat berjudul GAME RACE CAR. Gendre game ini merupakan game Balapan atau Race, karakter yang terdapat dalam game ini berupa mobil, berlatar di jalan raya yang banyak mobil lainnya. <p>

2. Story
   <p> Game Race Car merupakan game balap mobil yang dimana kita harus menyetir mobil di jalan raya dengan benar untuk mengindari mobil mobil lain atau mobil lawan (enemy) yang ingin menabrak kita selama waktu yang ada. Jika mobil yang kita kendarai menabrak mobil musuh maka game akan berakhir (kalah), jika kita berhasil menyetir mobil sampai waktu selesai, kita akan memenangkan game tersebut (menang). Jadi jika kita ingin memenangkan game tersebut kita harus mengindari mobil mobil musuh yang ingin menabrak kita dan terus bertahan sampai waktu yang ada habis. <p> 

3. Mechanic
    <p> Aksi utama dari Game Race Car selama gamenya berjalan adalah berpindah atau menhindar. Core Actionnya adalah move. dan Core Purpose adalah menghindari mobil lawan dari tabrakan. <p>

4. Aesthetic
    <p> Karakter dalam game ini memiliki mobil mobil yang keren, musik yang membuat enjoy dalam memainkan game ini membuat pemain lebih santai memainkannya dan efek yang memukau. <p>

5. Technology
    <p> Game yang kita buat menggunakan pygame dan game ini merupakan game yang berbasis desktop. <p>
       
### Pre-Production
**GAME DESIGN DOCUMENT**

**1. High Concept**
    <p> Game Race Car adalah game dimana pemain harus menyetir mobil untuk drag time atau balapan mobil di jalan yang lurus berpacuan waktu, sekaligus pemain harus menghindari halangan yang di buat oleh mobil lawan untuk menggagalkan kita mencapai garis finis. Cara mengatasi gangguan mobil musuh yang ingin menabrak kita, kita harus menghindarinya dengan berbelok ke kiri atau ke kanan. <p>
   
**2. Unique Value**
    <p> "Game Race Car" adalah game yang membutuhkan keterampilan dan singkronisasi kecepatan tangan. karen pemain harus berbelok ke kiri atau ke kanan untuk menghindari banyaknya mobil lawan yang akan menabrak kita. <p>
       
**3. Genre Game**
    <p> Kategori "Game Race Car" adalah ber Genre Balapan atau Race. <p>
       
**4. Target Audience**
    <p> "Game Race Car" merupakan game yang dapat dimainkan oleh golongan usia anak anak hingga dewasa. <p>
       
**5. Story**
    <p> "Game Race Car" Diawali mobil yang ingin balapan tetapi dihalangi oleh musuh musuh nya agar mobil tersebut tidak bisa mencapai garis finis. sehingga kita harus menyetir mobil tersebut agar dapat menghindari halangan halangan yang lawan berikan agar kita dapat memenangkan game tersebut. <p>
       
**6. Gameplay**
    <p> Pemain diminta untuk membantu mobil tersebut balapan di jalan agar bisa mencapai garis finis, dengan cara pemain akan diminta untuk menyetir mobil tersebut dijalan yang lurus dengan berbelok ke kiri atau ke kanan agar dapat menghindari tabrakan dari mobil mobil lawan sampai waktu yang ada habis. <p>
       
 # 4 Pilar OOP
       
 **1. Encapsulation**
      <p> Encapsulation merupakan proses di mana sebuah penanganan data ditempatkan di dalam wadah tunggal yang disebut sebagai class. Saat menggunakan encapsulation, data dapat diisolasi dan tidak dapat diakses langsung dari luar. Dengan begini, kita cukup menggunakan data tersebut tanpa harus tahu bagaimana proses yang terjadi sampai data tersebut bisa digunakan.<p>
a. Public
   <p>Ketika sebuah property atau method dinyatakan sebagai public, maka seluruh kode program di luar class bisa mengaksesnya, termasuk class turunan.<p>
b. Private
   <p>Jika sebuah property atau method di-set sebagai private, maka satu-satunya yang bisa mengakses adalah class itu sendiri. Class lain tidak bisa mengaksesnya, termasuk class turunan.<p>
c. Protected
   <p>Jika sebuah property atau method dinyatakan sebagai protected, berarti property atau method tersebut tidak bisa diakses dari luar class, namun bisa diakses oleh class itu sendiri atau turunan class tersebut.<p>
         
**2. Inheritance**
     <p> Inheritance memungkinkan kita untuk mendefinisikan sebuah class (induk) ke class baru (anak) dan memberi kita kesempatan untuk menggunakan member dari class yang diwariskan tersebut. Inheritance dapat didefinisikan juga sebagai proses di mana suatu objek memperoleh sifat dan perilaku dari objek lainnya.
Ketika ingin membuat class dengan fungsi yang sudah tersedia pada class lain, kita tidak perlu lagi menulis ulang kode tersebut di dalam class yang kita buat. Cukup dengan mewarisi class tersebut maka kita bisa langsung mengaksesnya.
Inheritance memiliki 5 jenis yaitu: <p>
1. Single inheritance,
   Suatu super class yang hanya memiliki satu sub class
2. Hierarchircal inheritance,
   Suatu super class yang memiliki beberapa sub class
3. Multiple inheritance,
   sebuah class yang dapat mewarisi lebih dari satu super class.
4. Multilevel inheritance,
   Suatu super class yang memiliki sub class , dan sub class memiliki turunan dari stuatu class
5. Hybrid inheritance,
   Merupakan gabungan dari single, multiple, multilevel, dan hierarchical
   
**3. Polymorphism**
   <p>Polymorphism merupakan kemampuan objek, variabel, atau fungsi yang dapat memiliki berbagai bentuk. Secara umum polymorphism dalam OOP terjadi ketika suatu SuperClass direferensikan ke dalam SubClass. Alhasil kita dapat mengembangkan sebuah program secara umum, bukan spesifik.<p>
