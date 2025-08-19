# List of State Codes
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Welcome:
print("Welcome to my program")

# Gather user information:
name = (input("What is your name?: ")).strip()

age = int(input(f"How old are you {name}?: "))

while True:
    location = (input(f'''Great! So your name is {name}, and you're {age} years old. Where are you located?
                  
                  You may enter: 
                  
                  AL, AK, AZ, AR, CA, CO, CT, DE, DC, FL,GA, HI, ID,
                  IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, MO,
                  MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, OR, PA,
                  RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY
                  
                  Enter State Here: ''')).upper()
    
    if location in states:
        print(f"{name}, you are {age} years old, and you are from {location}")
        break
    else:
        print("This is not an acceptable option. Please try again.")
