import statistics as s
import os
ele=[]
def main():
    os.system('cls')
    print("1.Mean\n2.Median\n3.mode\n4.exit\n")
    x=int(input("Enter your choice: "))
    if x==4:
        quit()
        
    os.system('cls')
    print("enter 'back' for result\n")
    while True:
        y=input("Enter Elements: ")               
        if y=="back":
            if x==1:
                mean()
            elif x==2:
                median()
            elif x==3:
                mode()
        else:
            y=int(y)
            ele.append(y)
def mean():
    os.system('cls')
    print("The mean is ",ele)  
    print("\nThe mean is ",s.mean(ele))
    q=input("press enter for main screen")
    y=input("Do you want to keep the data(Y/N): ")
    y=y.lower()
    if y=='n':
        ele=[]
    else:            
        main()
def median():
    os.system('cls')
    print("The elements are ",ele)
    print("\nThe median is ",s.median(ele))
    q=input("press enter for main screen")
    y=input("Do you want to keep the data(Y/N): ")
    y=y.lower()
    if y=='n':
        ele=[]
    else:       
        main()
def mode():
    os.system('cls')
    print("The elements are ",ele)
    print("\nThe mode is ",s.mode(ele))
    q=input("press enter for main screen")
    y=input("Do you want to keep the data(Y/N): ")
    y=y.lower()
    if y=='n':
        ele=[]  
    else:     
        main()    
main()            
        
        
        
    
