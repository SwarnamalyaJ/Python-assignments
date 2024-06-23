class multiplefunction():
    def oddEven():
        Number=int(input("Enter the number is Odd/Even="))
        if(Number%2)==0:
            message=print(Number,"Even Number")
        else:
            message=print(Number,"Odd Number")
        return message
    def EligibleforMarriage():
        Gender=input("Your Gender:")
        Age=int(input("Enter your age:"))
        if (Gender=="Male" and Age>21):
            message=print("Eligible")
        elif (Gender=="Female" and Age>18): 
            message=print("Eligible")             
        else:
            message=print("Not Eligible")
            return message
    def Subfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in List:
        print(temp)
    def  Tenthpercentage():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        total=(sub1+sub2+sub3+sub4+sub5)
        print("Total:",total)
        percentage=(total/5)
        print("Percentage",percentage)
        return percentage
    def triangle():
        Height=int(input("Height="))
        Breadth=int(input("Breadth"))
        area=Height*Breadth/2
        print("Areaoftriangle=",area)
        Height1=int(input("Height1="))
        Height2=int(input("Height2="))
        Breadth=int(input("Breadth"))
        perimeter=Height1+Height2+Breadth
        print("Perimeteroftriangle=",perimeter)