from tkinter import*
root=Tk()
root.title("Fibonacci sum")
root.geometry("500x500")

label_series=label_series(root, text="Fibonacci sum")
label_flower= Label(root)
label_spiral=Label(root)

def Fibonacci():
    number=10
    first_no=0
    second_no=1
    counter=1
    sum=0
    while(counter<=number):
        label_series["text"] += str(sum) + " "
        counter= counter+1
        first_no=second_no
        second_no=sum
        sum= first_no+second_no
        
        label_flower["text"]="Flower is fully bloomed"
        label_spiral["text"]="Spirals in right direction are"+ str(first_no) +"Spirals in left direction are"+ str(second_no)+ "\n Total number of spirals are "+ str(sum)
        
        
btn= Button(root, text="Show Fibonacci series", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()