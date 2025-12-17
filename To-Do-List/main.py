#Self Made To-Do List Code the way i want, So code the way you want Don't Copy anyone
# You can also use Def if you want 
task = []

while True:
    print("------Welcome to TO-DO List Application------",
          "1. Add Task",
          "2. Remove task",
          "3. View Tasks",
          "4. Update Tasks",
          "5. Exit", sep= "\n")             #sep is separating everyline here
    
    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        n = int(input("how many tasks you want to add?:"))           #...just looks good thats why i added this feature
        for i in range(0, n):
            add = input("Enter Your Task:")
            task.append(add)

    if choice == 2:
        rem = input("Enter The Task You Want To Remove:") # This one is imp in this program
        if rem in task:
            ind = task.index(rem)
            del task[ind]

    elif choice == 3:
        print("----Your Tasks----\n",task)                   
        
         # You can make it look more cool by printing each task separatly but this works for me 

    elif choice == 4:
        upd = input("Enter The Task You Want To Update:")
        if upd in task:
            up = input("Enter New Task:")
            ind = task.index(upd)
            task[ind] = up
    
    elif choice == 5:
        print("Thank You For Using To-Do List")
        break

    # GGs you are done