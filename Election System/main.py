def election_system():
    male_count = 0
    female_count = 0
    total_count = 0

    while True:
       try:
           age = int(input("Enter voter's age: "))
       
           if age < 18:
                print("You are ineligible to vote.")
                continue
        
           gender = input("Enter voter's gender (male/female): ").strip().lower()
    
           if gender == "male":
                male_count += 1
           elif gender == "female":
                female_count += 1
           else:
                print("Invalid gender entered.")
                continue
        
           total_count += 1
        
           another_voter = input("Is there another voter? (yes/no): ").strip().lower()
           if another_voter != "yes":
                break
       except ValueError:
            print("invalid value, Please enter a number")
            
    print(f"Male voters: {male_count}")
    print(f"Female voters: {female_count}")
    print(f"Total voters: {total_count}")

election_system()
