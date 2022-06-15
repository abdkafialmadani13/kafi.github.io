class siswa():
    def __init__(self,Nama,tmpt_lahir,tgl_lahir,nis,naik_tidak):
        self.Nama = Nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.nis = nis
        self.naik_tidak = naik_tidak
    def masuk (self,Nama,tmpt_lahir,tgl_lahir,nis,naik_tidak):
        self.Nama = Nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.nis = nis
        self.naik_tidak = naik_tidak
    def keluar (self):
        print('Nama Lengkap     :' + self.Nama)
        print('TTL           :' + self.tmpt_lahir + ','+ self.tgl_lahir)
        print('Nis           :' + self.nis)
        if self.naik_tidak >85:
            print('nilai A , naik kelas')
        else:
            if self.naik_tidak >75:
                print('nilai B , naik kelas')
            else:
                if self.naik_tidak >60:
                    print('nilai C , tidak naik kelas')

print('=================================')
print('     PROGRAM KENAIKAN KELAS      ')
print('=================================')
Nama    = input('Nama Lengkap              :')
tmpt_lahir  = input('Tempat Lahir             :')
tgl_lahir   = input('Tanggal Lahir             :')
nis         = str(input('Nis                  :'))
naik_tidak  = float(input('Masukkan Nilai Akhir   :'))

proses = siswa(Nama, tmpt_lahir, tgl_lahir, nis, naik_tidak)
print(proses.keluar())