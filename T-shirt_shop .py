import datetime
import smtplib
import random

def main():
    print("______ Welcome to TBOY TSHIRT ______")
    email = input("Please enter your email address: ")
    print("1. Men")
    print("2. Women")
    print("3. Kids")
    sel = int(input("Enter your choice: "))
    
    if sel == 1:
        men(email)
    elif sel == 2:
        women(email)
    elif sel == 3:
        kids(email)
    else:
        print("Invalid choice")
        main()

def men(email):
    print("___ For men you have ___")
    mshirt = 500
    mtshirt = 300
    mpants = 1000
    print("1. Shirt Rs 500")
    print("2. T-shirt Rs 300")
    print("3. Pant Rs 1000")
    selmen = int(input("Enter the product number: "))
    
    if selmen == 1:
        smen = int(input("Enter quantity: "))
        total = smen * mshirt
    elif selmen == 2:
        smen = int(input("Enter quantity: "))
        total = smen * mtshirt
    elif selmen == 3:
        smen = int(input("Enter quantity: "))
        total = smen * mpants
    else:
        main()
        
    print(f"Total amount: Rs {total}")
    bill(email, total)

def women(email):
    print("___ For women you have ___")
    wshirt = 500
    wtshirt = 300
    wpants = 1000
    print("1. Saree Rs 1000")
    print("2. T-shirt Rs 300")
    print("3. Pant Rs 500")
    selwom = int(input("Enter the product number: "))
    
    if selwom == 1:
        swomen = int(input("Enter quantity: "))
        total = swomen * wshirt
    elif selwom == 2:
        swomen = int(input("Enter quantity: "))
        total = swomen * wtshirt
    elif selwom == 3:
        swomen = int(input("Enter quantity: "))
        total = swomen * wpants
    else:
        main()
        
    print(f"Total amount: Rs {total}")
    bill(email, total)

def kids(email):
    print("___ For kids you have ___")
    kshirt = 200
    ktshirt = 100
    kpants = 300
    print("1. Shirt Rs 200")
    print("2. T-shirt Rs 100")
    print("3. Pant Rs 300")
    selkid = int(input("Enter the product number: "))
    
    if selkid == 1:
        skids = int(input("Enter quantity: "))
        total = skids * kshirt
    elif selkid == 2:
        skids = int(input("Enter quantity: "))
        total = skids * ktshirt
    elif selkid == 3:
        skids = int(input("Enter quantity: "))
        total = skids * kpants
    else:
        main()
        
    print(f"Total amount: Rs {total}")
    bill(email, total)

def bill(email, total):
    try:
        f = open("bill.txt", "a")
        x = datetime.datetime.now()    
        f.write(f"Total bill amount: Rs {total}\nTime & Date: {x}\nEmail Address: {email}\nThank You Come Again!!\n")    
        f.close()
        send_email(email, total)
    except Exception as e:
        print(f"Failed to generate bill: {e}")

def send_email(email, total):
    try:
        sender_email = "ranganathanm9324@gmail.com"  # Replace with your email address
        sender_password = ""  # Replace with your email password
        
        # Connect to the Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            
            message = f"Subject: Your Purchase Bill\n\nTotal amount: Rs {total}\n\nThank you for shopping with us!"
            server.sendmail(sender_email, email, message)
            
            print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
