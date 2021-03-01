# Nama			: Epata Tuah			   
# NIM			: 13519120			   
# Kelas			: K-03                             
# Mata Kuliah	: Strategi Algoritma               
# Deskripsi		: TUGAS KECIL 2 (Penyusunan Rencana Kuliah dengan Topological Sort)
#				  implementasi 13519120-main.py

#import other py
TS = __import__('13519120-topsort')
func = __import__("13519120-graphnfunc")

#Pembuka Program
print(" ____                                    _  __     _ _       _    ") 
print("|  _ \\ ___ _ __   ___ __ _ _ __   __ _  | |/ /   _| (_) __ _| |__ ") 
print("| |_) / _ \\ '_ \\ / __/ _` | '_ \\ / _` | | ' / | | | | |/ _` | '_ \\ ")
print("|  _ <  __/ | | | (_| (_| | | | | (_| | | . \\ |_| | | | (_| | | | |")
print("|_| \\_\\___|_| |_|\\___\\__,_|_| |_|\\__,_| |_|\\_\\__,_|_|_|\\__,_|_| |_|")
print("ASUMSI JUMLAH MATA KULIAH YANG DIAMBIL DIBAGI RATA KE 8 SEMESTER,")
print("         JUMLAH MATA KULIAH HARUS KELIPATAN ANGKA 8")
print("         KETIK FILE .txt YANG BERISI INPUT MATA KULIAH")
print("    BESERTA PREREQUISITE-NYA (misal 'test1' tanpa tanda petik)")
#input file yang akan disusun mata kuliahnya
inputAwal = str(input("                       Nama File : "))
fname = "../test/" + inputAwal + ".txt"

#Menyimpan daftar mata kuliah dengan memedulikan spasi (' ') 
with open(fname,'r') as f:
	courseList = []
	for line in f:
		word = []
		for character in line:
			if (character == ' '):
				continue
			if (character == ',' or character == '.'):
				break
			word.append(character)
		courseList.append(func.convert(word))

#Menyimpan daftar mata kuliah tanpa memedulikan spasi (' ') 
with open(fname,'r') as f:
	courseList2 = []
	for line in f:
		word = []
		for character in line:
			if (character == ',' or character == '.'):
				break
			word.append(character)
		courseList2.append(func.convert(word))

#Menyimpan daftar mata kuliah prerequisite tanpa memedulikan spasi (' ')
with open(fname, 'r') as f:
	coursePlan = []
	for line in f:
		coursePlan.append(func.preqCourse(line))

#Cek apakah jumlah mata kuliah pada file adalah kelipatan 8
if (len(courseList) % 8 != 0): #Jika tidak
	print("Jumlah mata kuliah bukan kelipatan 8! Silahkan ubah rencana mata kuliah Anda kembali.")
else: #Jika ya
	courseFix = []
	print()
	print("MATA KULIAH YANG DAPAT DIAMBIL PER SEMESTER:")
	#Memanggil prosedur topSort
	TS.topSort(courseFix, coursePlan, courseList, courseList2)		

        
