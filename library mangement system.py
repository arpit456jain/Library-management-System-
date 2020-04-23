def display(lst):
    print("in display function \n")
    for obj in lst:
        obj.display_book()

class library:
    name=""
    id=3
    issue='availbale'
    def __init__(self,gid,gname):
        self.name=gname
        self.id=gid
    
    def display_book(self):
        print("Book Name: {}  \t Book id : {}  \t Availablity :{} ".format(self.name,self.id,self.issue))
        
    def add_book(self):
       lst.append(self)
       print("book is added succesfully!!")

   
    @staticmethod
    def issue_book(bname):
       for obj in lst:
           if obj.name==bname:
               print("found")
               if obj.issue =='availbale':
                   print('book is availale')
                   obj.issue = 'not available'
                   break
               else:
                   print("book is not availblle rigth now")
                   break
       else:
           print("book is not in the lib")

    def return_book(bname):
        for obj in lst:
            if obj.name==bname:
                print("this book is isseud from lib")
                obj.issue='available'
                print("you have succesfully returned the book")

    
class student:
    roll_no=0
    name=""
    def __init__(self,groll,gname):
        self.name=gname
        self.roll_no=groll
    def add_student(self):
        lst1.append(self)
        print("your account is added")
        

        
    
if __name__=="__main__":
    book1=library(1,'phy')
    book2=library(2,'chem')
    book3=library(3,'math')
    lst=[book1,book2,book3]
        
    aj1=student(101,'arpit')#by default user
    lst1=[aj1]
    
    while(1):
        #initially books in library available
        print("\n\nWhat do you want initially my libary has 3 books you can check it")
        print("1 for issue a book")
        print("2 for return a book")
        print("3 for donating a book")
        print("4 for display which book is avalible")
        ch=input("enter your choice")
        if ch=='4':
            display(lst)
        elif ch=='3':
            add_book=input("enter the name of book")
            library.id=library.id+1
            id=library.id
            book=library(id,add_book)
            print("book obj is succesfully created")
            book.add_book()

        elif ch=='1':
            user=input("press yes if you are an new user otherwise press no")
            if user=='yes':
                user_name=input("enter your name")
                user_roll=int(input("enter your roll no"))
                new_user=student(user_roll,user_name)
                new_user.add_student()
                
                
            bname = input('which book do you want to isse!! enter the name')
            library.issue_book(bname)

        elif ch=='2':
            bname = input('which book do you want to return!! enter the name')
            library.return_book(bname)
            
        else:
            print("wrong choice")

