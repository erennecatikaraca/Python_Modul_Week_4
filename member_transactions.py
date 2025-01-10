import json,os,string
from datetime import datetime,timedelta
memberPath = 'member.json'
trackingPath = 'tracking.json'
bookPath = 'book.json'



def memberList():

    if os.path.exists(memberPath):
        with open(memberPath,"r",encoding="utf-8") as file:
            data = json.load(file)
            if data:
                print(f"Total member: {len(data)}")
                for dicts in data:
                    print("")
                    for key, value in dicts.items():
                        print(f"{key}: {value}")
            else:
                print("there is no data in the list!")
    else:
        print("the file not found!")


def addMember():
    id = 1
    flag = False
    with open(memberPath,"r") as file:
        data = json.load(file)
        if len(data)>0:
           id += (data[-1]['id'])
            
    while True:
        memberDict = {}
        memberName = input("please enter the member's name: ").strip().title()
        telNo = input("please enter your telophone number: ")
        adres = input("please enter your adres: ").title()
        memberDict["id"] = id
        memberDict["Member Name"]=memberName
        memberDict["Tel"] = telNo
        memberDict["adress"] = adres

        with open(memberPath,'r+',encoding='utf-8') as file2:
            data2 = json.load(file2)
            data2.append(memberDict)
            file2.seek(0)
            json.dump(data2,file2,ensure_ascii=False,indent=4)
            
        
        while True:
            ques = input("Do you want to add more member?  Y/N: ").strip().upper()
            if ques == "N":
                flag = True
                break
            if ques == "Y":
                id += 1
                break
            elif ques not in ("Y","N"):
                print("invalid input!")
        if flag == True:
            break
            
def searchMember():
    flag = False
    with open(memberPath,"r",encoding="utf-8") as file:
        data = json.load(file)
        if data:
            while True:
                memberName = input("please enter the member's name: ").title()
                for dict in data:
                    if dict["Member Name"] == memberName:
                        print("")
                        flag = True
                        for key, value in dict.items():
                            print(f"{key}: {value}")
                    
                if flag == False:
                    print("The member can not be found!")            
                else:
                    break        
        else:
            print("There is no member to display!")

def deleteMember():
    flag = False
    with open(memberPath,"r",encoding="utf-8") as file:
        data = json.load(file)
    if data:
        while True:
            memberName = input("please enter the member name: ").strip().title()
            for dict in data:
                if memberName in dict["Member Name"]:
                    flag = True
                    break
                    
            else:
                print("the member can not be found! please try again")
                continue
            if flag == True:
                newMember = [dict2 for dict2 in data if dict2["Member Name"] != memberName]
                with open(memberPath, "w", encoding="utf-8") as file2:
                    json.dump(newMember,file2,ensure_ascii=False,indent=4)
                    break
    else:   
        print("there is no member to display!")



def bookRental():
    counter_id = 1
    rentalDict = {}
    with open(trackingPath,"r",encoding="utf-8") as trackingFile1:
        trackingData1 = json.load(trackingFile1)
        if trackingData1:
            counter_id += trackingData1[-1]["id"]
    with open(bookPath,"r",encoding="utf-8") as bookFile:
        bookData = json.load(bookFile)
    with open(memberPath,"r",encoding="utf-8") as memberFile:
        memberData = json.load(memberFile)
    if bookData and memberData:
        
        while True:
            bookName = string.capwords(input("please enter the book's name: "))
            memberName = input("please enter the member's name: ").title()
            for memberDict in memberData:
                for bookDict in bookData:
                    if memberName == memberDict["Member Name"] and bookName == bookDict["Kitap_Adi"]:
                        rentalDict["id"] = counter_id
                        rentalDict["Member Name"] = memberDict["Member Name"]
                        rentalDict["Tel"] = memberDict["Tel"]
                        rentalDict["Adres"] = memberDict["adress"]  
                        rentalDict["Barcode"] = bookDict["Barkod"]
                        rentalDict["Language"] = bookDict["Dil"]
                        rentalDict["Price"] = bookDict["Fiyat"]
                        rentalDict["Book Name"] = bookDict["Kitap_Adi"]
                        rentalDict["Publisher"] = bookDict["Yayinevi"]
                        rentalDict["Author"] = bookDict["Yazar"]
                        rentalDict["Transaction Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        return_date = datetime.now() + timedelta(weeks=2)
                        rentalDict["Return Date"] = return_date.strftime("%Y-%m-%d %H:%M:%S")

                        with open(trackingPath, "r+", encoding="utf-8") as trackingFile2:
                            trackingData2 = json.load(trackingFile2)
                            trackingData2.append(rentalDict)  
                            trackingFile2.seek(0)  
                            json.dump(trackingData2, trackingFile2, ensure_ascii=False, indent=4)
                        removedBookJson = [bookDict2 for bookDict2 in bookData if bookDict2["Kitap_Adi"]!=bookName]
                        with open(bookPath,"w",encoding="utf-8") as bookFile2:
                            json.dump(removedBookJson,bookFile2,ensure_ascii=False,indent=4)
                            print("the book has been rented")
                        break
                else:
                    continue  
                break
            else:
                print("Member name or book title not found, please try again.")
                continue
            break

    else:
        print("There is no registered member or book in the system!")
        return


def returnBook():
    addBook = {}
    with open(trackingPath,"r", encoding="utf-8") as trackingFile:
        data = json.load(trackingFile)
        if data:
            while True:
                memberName = input("please enter the member's name: ").title()
                bookName = string.capwords(input("please enter the book's name: "))
                for dict in data:
                    if dict["Member Name"] == memberName and bookName == dict["Book Name"]:
                        break

                else:
                    print("member not found please try again")
                    continue
                break
        else:
            print("there is no book to return")
            return  
    
    with open(trackingPath,"r+",encoding="utf-8") as trackingFile_2:
        trackingData2 = json.load(trackingFile_2)
        for dictTrack in trackingData2: # return islemi yapilcak olan kitabi geri kitap kutuphanesine gondermek icin sozluge ekleme
            if memberName == dictTrack["Member Name"] and bookName == dictTrack["Book Name"]:
                addBook["Barkod"] = dictTrack["Barcode"]
                addBook["Dil"] = dictTrack["Language"]
                addBook["Fiyat"] = dictTrack["Price"]
                addBook["Kitap_Adi"] = dictTrack["Book Name"]
                addBook["Yayinevi"] = dictTrack["Publisher"]
                addBook["Yazar"] = dictTrack["Author"]
    
    newTracking = [dictTrack2 for dictTrack2 in trackingData2 if not (memberName == dictTrack2["Member Name"] and bookName == dictTrack2["Book Name"])]
    print(f"newTracking sozlugu: {newTracking}")
    with open(trackingPath, "w") as trackingFile_3:
        json.dump(newTracking,trackingFile_3, ensure_ascii=False,indent=4)
        print("the book has been returned")

    with open(bookPath,"r+",encoding="utf-8") as bookFile:
        bookData = json.load(bookFile)
        bookData.append(addBook)
        bookFile.seek(0)
        json.dump(bookData,bookFile, ensure_ascii=False,indent=4)

            

def bookTracking():
    with open(trackingPath,"r", encoding="utf-8") as file:
        data = json.load(file)
        if data:
            print("")
            for dict in data:
                for key, value in dict.items():
                    print(f"{key}: {value}")
        else:
            print("there is no book to track!")
