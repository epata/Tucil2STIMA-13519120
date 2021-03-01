# Nama			: Epata Tuah			   
# NIM			: 13519120			   
# Kelas			: K-03                             
# Mata Kuliah	: Strategi Algoritma               
# Deskripsi		: TUGAS KECIL 2 (Penyusunan Rencana Kuliah dengan Topological Sort)
#				  implementasi 13519120-topsort.py

#import other py
func = __import__("13519120-graphnfunc")

#Algoritma Topological Sort
def topSort(courseFix, coursePlan, courseList, courseList2):
	#Inisialisasi i dan j
	i = 0
	j = 0
	#Cek apakah semua simpul pada DAG terpilih
	if (len(coursePlan) == 0): #Jika semua simpul telah terpilih
		func.outputPembagianMatKul(courseFix, 8)
	else: #Jika ada simpul yang belum terpilih
		while (i < len(coursePlan)) :  #selama ketemu simpul yang derajat masuknya bukan nol, dilakukan perulangan while
			if (len(coursePlan[i]) == 0): #Jika derajat masuk = 0 (prerequisite nol)
				tempCourse = courseList[i] #simpan nama mata kuliah tersebut di tempCourse (sementara)

				#terdapat courseList dan courseList2 untuk kasus input mata kuliah prerequisite pada file .txt
				#yang memiliki spasi setelah mata kuliah non-prerequisite 

				courseFix.append(courseList2[i]) #Tambahkan mata kuliah tersebut di array courseFix
				courseList2.pop(i) #Hilangkan simpul mata kuliah tersebut pada array courseList2
				courseList.pop(i) #Hilangkan simpul mata kuliah tersebut pada array courseList
				coursePlan.pop(i) #Hilangkan himpunan kosong ([] karena prerequisite simpul mata kuliah tersebut nol) pada array coursePlan

				#Hapus semua busur yang keluar dari simpul mata kuliah tersebut
				for i in range(len(coursePlan)):
					if (func.indeksAdaCourse(tempCourse, coursePlan[i])):
						func.hapusCourse(tempCourse,coursePlan[i])
				break #stop perulangan karena sudah menemui simpu yang derajat masuk = 0
			i+=1
		#Panggil kembali fungsi topSort (rekursif) hingga semua simpul DAG terpilih (array coursePlan habis)	
		topSort(courseFix, coursePlan, courseList, courseList2)