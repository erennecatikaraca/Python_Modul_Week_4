import json,random,string
bookPath = "book.json"

def bookList():
    with open(bookPath,"r", encoding='utf-8') as file:
        data = json.load(file)
        if data:
            print("\n____BOOK LIST____")
            print(f"\nTotal Books: {len(data)}")
            for dict in data:
                print("")
                for key, value in dict.items():
                    print(f"{key}:{value}")
        else:
            print("there is no book to display")

def addBook():
    addition = {}
#-------------barcode generate-------------------------------
    number = '978605'
    while True:
        number2 = ''
        for _ in range(7):
            number2 += str(random.randint(0,9))
        with open(bookPath,"r",encoding="utf-8") as file:
            data = json.load(file)
            if data:
                for dicts in data:
                    if int(number+number2) == dicts["Barkod"]:
                        continue
                    else:
                        barcode = int(number+number2)
                        break
            else:
                barcode = 9786053214582
                break
        break

#-------------barcode generate---------------------------------
    while True:
        Dil = input("lutfen kitabin dilini giriniz: ").title()
        while True:
            Fiyat = input("lutfen kitap fiyatini giriniz: ")
            try:
                Fiyat = float(Fiyat)
                break
            except ValueError:
                print("lutfen sayi giriniz!")
        Kitap_adi = string.capwords(input("lutfen kitap ismini giriniz: "))
        Yayinevi = input("lutfen yayinevi adini giriniz: ").title()
        Yazar = input("lutfen kitabin yazarini giriniz: ").title()
        addition['Barkod']=barcode
        addition['Dil']=Dil
        addition['Fiyat']=Fiyat
        addition['Kitap_Adi']=Kitap_adi
        addition['Yayinevi']=Yayinevi
        addition['Yazar']=Yazar
        with open(bookPath,"r+",encoding="utf-8") as file:
            data = json.load(file)
            data.append(addition)
            file.seek(0)
            json.dump(data,file,ensure_ascii=False,indent=4)
        break
    while True:
        ques = input("baska kitap eklemek istermisiniz?  Y/N: ").strip().upper()
        if ques == "N":
            print("cikis yapiliyor")
        elif ques == "Y":
            addBook()
        else:
            print("yanlis giris yaptiniz")
            continue
        break
        


def searchBook():
    flag = False
    while True:
        bookName = string.capwords(input("please enter the book name: "))
        with open(bookPath,"r",encoding="utf-8") as file:
            data = json.load(file)
        for dicts in data:
            if bookName == dicts["Kitap_Adi"]:
                print("")
                for key, value in dicts.items():
                    print(f"{key}: {value}")
                    flag = True
        if flag == True:
            break
        else:
            print(f"{bookName} cannot be found please try again")

def removeBook():
    flag = False
    while True:
        removedBook = string.capwords(input("please enter the book name: "))
        with open(bookPath,"r",encoding="utf-8") as file:
            data = json.load(file)
            for dicts in data:
                if dicts["Kitap_Adi"] == removedBook:
                    flag = True
        if flag == True:
            break
        else:
            print(f"{removedBook} can not be found int the book list please try again")

    newJson = [dicts2 for dicts2 in data if dicts2["Kitap_Adi"] != removedBook]
    with open(bookPath,"w") as file:
        json.dump(newJson, file,ensure_ascii=False, indent=4)
    print("the book has been removed")

        
