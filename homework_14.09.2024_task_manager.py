class ToDoList:
    def __init__(self):
        self.lst = []

    def add_task(self):
        self.lst.append(input("Enter a task: ---> "))
        print("task was added successfully")
        print(self.lst)
    def edit_task(self):
        self.c = int(input("enter index number you wish to edit: "))
        self.oldtask = self.lst[self.c]
        self.lst[self.c] = input(f"enter a new task to overwrite {self.lst[self.c]}")
        print(f"{self.oldtask} has been successfully changed to {self.lst[self.c]}")
        print(f"{self.lst}")

    def del_task(self):
        print(self.lst)
        self.d = int(input("delete a task you wish. enter index number---> "))
        print(f"{self.lst[self.d]} has been successfully deleted")
        del self.lst[self.d]
        print(self.lst)

    def show(self):
        print(self.lst)

obj1 = ToDoList()


while True:
    a = input("enter 1 to 'add' task \n"
              "enter 2 to 'edit' task \n"
              "enter 3 to 'delete' task \n"
              "enter 4 to 'print' task \n"
              "enter 5 or type 'exit' to exit program \n"

              "Select an option: ")

    if a=="1":
        obj1.add_task()
    elif a=="2":
        obj1.edit_task()
    elif a=="3":
        obj1.del_task()
    elif a=="4":
        obj1.show()
    elif a=="5":
        break


#     if a=="1":
#         b = input("enter your task:")
#         lst.append(b)
#         print("Task was added successfully")
#         print(lst)
#     if a=="2":
#         print(lst)
#         c = int(input("enter index number you wish to edit --->"))
#         oldtask = lst[c]
#         lst[c] = input(f"enter a new task to overwrite {lst[c]}--->")
#         print(f"{oldtask} has been successfully changed to {lst[c]}")
#         print(lst)
#     if a=="3":
#         print(lst)
#         d = int(input("delete a task you wish. enter index number --->"))
#         print(f"{lst[d]} has been successfully deleted!")
#         del lst[d]
#         print(lst)
#     if a=="4":
#         print(lst)
#     if a=="5" or a=="exit":
#         print("Exiting now. Good bye!")
#         break


