# Nama			: Epata Tuah			   
# NIM			: 13519120			   
# Kelas			: K-03                             
# Mata Kuliah	: Strategi Algoritma               
# Deskripsi		: TUGAS KECIL 2 (Penyusunan Rencana Kuliah dengan Topological Sort)
#				  implementasi 13519120-graphnfunc.py

#FUNGSI-FUNGSI ESENSIAL YANG DIGUNAKAN PADA 13519120-main.py dan 13519120-topsort.py
#Fungsi convert(arrayOfChar) menyatukan isi arrayOfChar menjadi sebuah kata
def convert(arrayOfChar): 
    new = "" 
    for x in arrayOfChar: 
        new += x   
    return new 

#REPRESENTASI DAG (DIRECTED ACYCLIC GRAPH)
#Fungsi preqCourse(lineSemester) mengembalikan array preqList dari suatu line kata 
#array preqList berisi simpul-simpul mata kuliah prerequisite tujuan dari suatu simpul mata kuliah
def preqCourse(lineSemester):
	preqList = []
	word = []
	i = 0
	for character in lineSemester:
		if (character == ' '):
					continue
		if (character == ',' or character == '.'):
			i+=1
			if (i==1):
				word = []
				continue
			else:
				preqList.append(convert(word))
				word = []
				continue
		word.append(character)
	return(preqList)

#Fungsi indeksAdaCourse(erasedCourse, coursePlan) mengecek apakah terdapat kata pada array coursePlan yang
#merupakan kata erasedCourse
def indeksAdaCourse(erasedCourse, coursePlan):
	for word in coursePlan:
		if (word == erasedCourse):
			return True
	return False

#Prosedur hapusCourse(erasedCourse, coursePlan) menghapus mata kuliah pada array coursePlan berisi
#prerequisite course yang mata kuliahnya adalah erasedCourse (menghapus busur masuk pada simpul mata kuliah
#yang terhubung pada simpul mata kuliah erasedCourse yang telah dihapus)
def hapusCourse(erasedCourse, coursePlan):
	for i in range(len(coursePlan)):
		if (coursePlan[i] == erasedCourse):
			coursePlan.pop(i)
			break

#OUTPUT
#Prosedur outputPembagianMatkul(courseFix, jumlahSemester) digunakan untuk mengeluarkan output mata kuliah yang
#harus diambil per semester
def outputPembagianMatKul(courseFix, jumlahSemester):
	if (jumlahSemester == 8):
		matkulPerSemester = int(len(courseFix)/jumlahSemester)
		iSemester = 1
		iHitungCourse = 0
		iCurrCourse = 0
		while (iSemester <= 8):
			hitungKoma = 0
			print("Semester", iSemester, ": ", end='')
			while (iCurrCourse<(matkulPerSemester+iHitungCourse)):
				if (matkulPerSemester>1):
					if (hitungKoma==matkulPerSemester-1):
						print(courseFix[iCurrCourse], end='')
					else:
						print(courseFix[iCurrCourse], end='')
						print(', ', end='')
						hitungKoma+=1
				else:
					print(courseFix[iCurrCourse])
				iCurrCourse+=1
			iHitungCourse += matkulPerSemester
			iSemester+=1
			if (matkulPerSemester>1):
				print()
