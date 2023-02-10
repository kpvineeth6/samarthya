vowels = 0;  
consonants = 0;  
str = str(input("enter a string:"))  
   
#Converting entire string to lower case to reduce the comparisons  
str = str.lower();  
for i in range(0,len(str)):   
    #Checks whether a character is a vowel  
    if str[i] in ('a',"e","i","o","u"):  
        vowels = vowels + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        consonants = consonants + 1;  
print("Total number of vowel and consonant are" );  
print("vowels=",vowels);  
print("consonants",consonants)