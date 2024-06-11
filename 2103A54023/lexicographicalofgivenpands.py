#Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?
#You are given a string P that denotes the new order of letters in the English dictionary.
#You need to print the smallest lexicographic string made from the given string S.
#Constraints: 1 <= T <= 1000
#Length (P) = 261 <= length (S) <= 100
#All characters in the string S, P are in lowercase
#Input Format
#The first line contains number of test cases T
#The second line has the string P
#The third line has the string S
#Output
#Print a single string in a new line for every test case giving the result

# Function to transform string S into the smallest lexicographic string based on the order specified by string P
tcase=int(input())
for i in range(tcase):
    lexi=input()
    s=input()
    for i in range(len(lexi)):
        c=lexi[i]
        if c is s:
            print(c,end='')