s=input("enter a string:").lower()
count=0
vowels="aeiou"
for ch in s:
   if ch in vowels:
      count+=1
print("number of vowels:",count)