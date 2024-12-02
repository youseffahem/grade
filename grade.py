"""
Write a program that assigns a letter
grade based on a student's score. Here are
some conditions:
If the score is 90 or above, print "A -
Excellent work!"
Else if the score is 80 or above, print "B
- Great job!"
Else if the score is 70 or above, print "C
- You did alright."
Else if the score is 60 or above, print "D
- Needs improvement."
Else, print "F - Study harder next time."
*Get the score from the use
"""
score=float(input("Enter your score : "))

if score>=90:
    print("A")
elif score >=80 and score <=90:
    print("B")   
    
elif score >=70 and score <=80:
    print("C")    
        
elif score >=60 and score <=70:
    print("D")    
    
else:
    print("F - Study harder next time.")
