def count_vowels():
 A=str(input("ENTER YOUR STRING:"))
 count=0
 for i in A:
    
    if (i=='A'or i=='E'or i=='I'or i=='O' or i=='U' or i=='a' or i=='e' or i=='i'or i=='o' or i=='u'):
        count= count + 1


 print("NUMBER OF VOWELS ARE",count)

count_vowels()
