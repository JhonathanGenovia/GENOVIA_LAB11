name = input("Enter Your Name:")
section = input ("Enter Your Section:")
prelim = float(input("Enter Your Prelim Grade:")) 
midterm = float(input("Enter Your Midterm Grade:")) 
finals= float(input("Enter Your Finals Grade:")) 
grade = (prelim + midterm + finals) /3

if prelim <= 40 or grade >= 101:
    print("Invalid")
elif midterm <= 40 or grade >= 101:
    print("Invalid")
elif finals <= 40 or grade >= 101:
    print("Invalid")
elif grade >= 99 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 1.00 Excellent")
elif grade >= 96 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 1.25 Outstanding")
elif grade >= 93 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 1.50 Superior")
elif grade >= 90 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 1.75 Very Good")
elif grade >= 87 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 2.00 Good")
elif grade >= 84 : 
    print ("Final Grade:" ,round(grade) , "Your GPA Is 2.25 Satisfactory")
elif grade >= 81 : 
    print ("Final Grade:" ,round(grade) , "Your GPA Is 2.50 Fairly Satisfactory")
elif grade >= 78 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 2.75 Fair")
elif grade >= 75 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 3.00 Passed")
elif grade <75 :
    print ("Final Grade:" ,round(grade) , "Your GPA Is 5.0 Failed")