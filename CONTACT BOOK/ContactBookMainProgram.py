from ContectBookMenu import menu
from ContectBookOperation import addinformation,viewcontactlist,searchcontact,updatecontact,Deletecontact
while(True):
    menu()
    ch=int(input("Enter ur choice:"))
    match(ch):
        case 1:
            print("To add the contact information:")
            addinformation()
        case 2:
            print("To view the contact list:")
            viewcontactlist()
        case 3:
            print("To search for the contact:")
            searchcontact()
        case 4:
            print("To update the contact:")
            updatecontact()
        case 5:
            print("To delete the contact:")
            Deletecontact()
        case 6:
            print("Thanks for using program")
            break


