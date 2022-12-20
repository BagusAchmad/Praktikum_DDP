inp = int(input("Masukkan jumlah nilai yang anda butuhkan untuk rata-rata ="))#Memasukkan jumlah angka yang akan di rata-rata
total = 0 #variabel total diberikan nilai 0
for i in range(inp):#pernyataan loop for di dalam bahasa pemrograman Python. 
    nilai = int(input("masukan nilai: "))#variabel nilai diberikan nilai yang diinput oleh pengguna melalui perintah input.
    total += nilai #variabel nilai akan ditambahkan ke nilai yang disimpan dalam variabel total, dan hasilnya akan disimpan kembali ke dalam variabel total.
 
ratarata = total / inp#pembagian dari variabel total dan inp akan disimpan ke dalam variabel ratarata.

print("rata rata: ", ratarata)#Pesan "rata rata: " dan nilai dari variabel ratarata akan dicetak ke layar.