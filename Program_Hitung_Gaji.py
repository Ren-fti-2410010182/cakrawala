print('Program Hitung Gaji Karyawan')
print('----------------------------\n')

nama = str(input('Masukan Nama Karyawan : '))
nik = int(input('Masukan  Nik  Karyawan :'))
masakerja = int(input('Masukan Masa Kerja (dalam tahun) :'))
status = str(input('Masukan Status Karyawan (Tetap/Kontrak) : '))
statushub = str(input('Masukan Status Hubungan  (Belum Menikah/Menikah) :'))
gajipokok = int(input('Masukan Gaji Pokok : '))

if (masakerja > 5) :
    bonus = gajipokok * 0.15
else :
    bonus = 0

if status == 'Tetap' :
    uangstran = 50000
else : 
    uangstran = 0

if statushub == 'Menikah' :
    tunjangan = gajipokok * 0.10
else :
    tunjangan = 0

gajibersih = gajipokok + bonus + tunjangan + uangstran

print('')
print('===== Rincian Gaji Karyawan =====')
print('Nama Karyawan   : ', nama)
print('Nik Karyawan    : ', nik)
print('Masa Kerja      : ', masakerja, 'Tahun' )
print('Status Karyawan : ',status )
print('Status Hubungan : ',statushub)
print('Gaji Pokok      : Rp.', gajipokok)
print('Bonus           : Rp.',bonus)
print('Uang transport  : Rp.',uangstran)
print('Tunjangn        : Rp.',tunjangan)
print('Gaji Bersih     : Rp.', gajibersih)