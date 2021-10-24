'''
berikut saya lampirkan program 2 dari modul 4
dengan ketentuan yang telah diberikan, dengan sedikit
modifikasi dari program 1, dengan menggunakan function()
sebagai loop dan dictionary.
'''

def data_mahasiswa() :
    print ("------------------------------------")
    print ("|Please type the input as requested|")
    print ("------------------------------------")
    nama = str(input("|Your name = "))
    nom = int(input("|Your NIM = "))
    age = int(input("|Your age = "))
    date = str(input("|Your date of birth (in numeric, example : 24-09-2003) = "))
    tinggi = float(input("|Your Height (in meters, example : 1.60) = "))
    hasil = {
        "Name = ": nama,
        "NIM = ": nom,
        "Age = ": age,
        "Date of birth =" : date,
        "Height = " : tinggi
    }
    print ("|---------------------------------------Processing--|")
    print ("|--------------------------Processing---------------|")
    print ("|-------------Processing----------------------------|")
    print ("|Processing-----------------------------------------|")
    print ("|---------------------------------------------------|")
    print ("|--------Would you like to see the results?---------|")
    print ("|---------------------------------------------------|")
    worc = str(input("|Please type YES for results = "))
    print (("=")*122)
    print ("|| LIST = ", hasil,("||"))
    print (("=")*122)
    print ("|---------------------------------------------------|")
    print ("|-----------Do you want to end the program?---------|")
    print ("|------------------------or-------------------------|")
    print ("|--------------Continue inputting data?-------------|")
    print ("|---------------------------------------------------|")
    choi = (str(input("|Please type YES to end or NO to input more data = ")))
    if choi == ("YES") or choi == ("Yes") or choi == ("yes") :
        print ("=======================================")
        print ("| Thank you for using me, Good bye :) |")
        print ("=======================================")
    else :
        data_mahasiswa()

    
print ("|------------------------------------------------|")
print ("|-Halo, Selamat Datang di Program Data Mahasiswa-|")
print ("|-------Made by Felix Christopher Afrian---------|")
print ("|------------------------------------------------|")
print ("|------------Type \"mulai\" to enter---------------|")
x = str(input("|Please type here = "))
if x == ("mulai") or x == ("Mulai") or x == ("MULAI") :
    data_mahasiswa()