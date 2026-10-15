# #functions
def greet():#function def
    print("hi jagan")
greet()
greet()

def addition(a,b):
    print(a+b)

    addition(5,6)
    addition(100,200)
    addition(200,300)

    def multiplication(a,b,c):
        return a*b*c
    result=multiplication(5,5,5)
    print(result)

    #global variable and local variable
    def collage():
        text="message" #local variable
        print(text)
    collage()
    message="hello" #global variable
    def google():
        print(message)
    google()