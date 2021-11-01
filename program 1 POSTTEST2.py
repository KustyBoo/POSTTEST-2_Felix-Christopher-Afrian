'''
disini saya melampirkan program pertama dari modul 4
menggunakan loop dan tampilan.

'''
print ("      /   \                          /  \                          ")
print ("     /  /\ \                        / /\ \                         ")
print ("    /  /  \ \                      / /  \ \                        ") 
print ("   /  /    \ \                    / /    \ \                       ")
print ("  /  /      \ \                  / /      \ \                      ")
print (" /  /        \ \    KustyBoo    / /        \ \                     ")
print ("/  /          \ \______________/ /          \ \                    ")
print("|                                               |                   ")
print("|         000                     000           |                   ")
print("|        0 | 0                   0 | 0          |                   ")
print("|        0 | 0                   0 | 0          |                   ")
print("|        0 | 0          |        0 | 0          |                   ")
print("|          0           |           0            |                   ")
print("|                       |                       |                   ")
print("|                                               |                   ")
print("|             ||      |||||      ||             |                   ")
print("|              ||    ||   ||    ||              |                   ")
print("|               ||||||     ||||||               |                   ")
print("|                                               |                   ")
print("|                                               |                   ")
print("|_______________________________________________|                   ")
print("|===================== uwu =====================|")
print ("|-----------------------------------------------|")
print ("|-Halo, Selamat Datang di Program Konversi Suhu-|")
print ("|-------Made by Felix Christopher Afrian--------|")
print ("|-----------------------------------------------|")
print ("|------------Type \"mulai\" to enter--------------|")
x = str(input("|Please type here = "))
y = 1
while y > 0 :
    if x == ("mulai") or x == ("Mulai") or x == ("MULAI") :
        print ("|----------------------------------------------------|")
        print ("|Please Choose which temperature you want to converse|")
        print ("|-------------------- a, b, or c ? ------------------|")
        print ("|----------------------------------------------------|")
        print ("|a. Fahrenheit to Celsius|")
        print ("|b. Kelvin to Celsius    |")
        print ("|c. Reamur to Celsius    |")
        pilihan = str(input("Please type your choice here = "))
        temp = float(input("Please type your temperature here = "))
        fh = ((temp) - 32) * 5/9
        kel = (temp) - 273
        re = (temp) * 5/4
        if pilihan == ("a") or pilihan == ("A") :
            print ("---------------------------------")
            print ("|RESULTS = ", fh,(" |"))
            print ("---------------------------------")
        elif pilihan == ("b") or pilihan == ("B") :
            print ("---------------------------------")
            print ("|RESULTS = ", kel,(" |"))
            print ("---------------------------------")
        elif pilihan == ("c") or pilihan == ("C") :
            print ("---------------------------------")
            print ("|RESULTS = ", re,(" |"))
            print ("---------------------------------")
        print ("---------------------------------------------------------")
        print ("|Do you wish to continue conversing another temperature?|")
        print ("-----------------------|YES or NO|-----------------------")
        wish = str(input("|Please type here = "))
        x = 1
        while x > 0 :
            if wish == ("YES") or wish == ("yes") or wish == ("Yes") :
                print ("|----------------------------------------------------|")
                print ("|Please Choose which temperature you want to converse|")
                print ("|-------------------- a, b, or c ? ------------------|")
                print ("|----------------------------------------------------|")
                print ("|a. Fahrenheit to Celsius|")
                print ("|b. Kelvin to Celsius    |")
                print ("|c. Reamur to Celsius    |")
                pilihan = str(input("Please type choice here = "))
                temp = float(input("Please type your temperature here = "))
                fh = ((temp) - 32) * 5/9
                kel = (temp) - 273
                re = (temp) * 5/4
                if pilihan == ("a") or pilihan == ("A") :
                    print ("---------------------------------")
                    print ("|RESULTS = ", fh,(" |"))
                    print ("---------------------------------")
                elif pilihan == ("b") or pilihan == ("B") :
                    print ("---------------------------------")
                    print ("|RESULTS = ", kel,(" |"))
                    print ("---------------------------------")
                elif pilihan == ("c") or pilihan == ("C") :
                    print ("---------------------------------")
                    print ("|RESULTS = ", re,(" |"))
                    print ("---------------------------------")
                print ("---------------------------------------------------------")
                print ("|Do you wish to continue conversing another temperature?|")
                print ("-----------------------|YES or NO|-----------------------")
                wish = str(input("|Please type here = "))
            
            else :
                print ("---------------------------------------------")
                print ("|My purpose have been fulfilled, Good Bye :)|")
                print ("---------------------------------------------")
                break
    else :
        print ("|---------------------------------------------------------------------------|")
        print ("|oops, it seems that you have not entered the word \"mulai\", please try again|")
        print ("|-------------------------Type \"mulai\" to enter-----------------------------|")
        x = str(input("|Please type here = "))
        continue
    break
print ("done")
