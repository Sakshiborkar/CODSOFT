from Menu import menu
from OpreationsEx import addop,subop,mulop,divop,moddivop,expop
while(True):
    try:
      menu()
      ch=int(input("Enter ur choice:"))
      match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            moddivop()
        case 6:
            expop()
        case 7:
            print("Thank you for using this program")
            break
        case _:
            print("your selection of operation is wrong--try again")
    except ValueError:
        print("Dont enter alnum,str and symbols")
