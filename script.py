import os
import mysql.connector
from colorama import Fore, Back, Style

db = mysql.connector.connect(
    host = 'localhost',
    user = 'UserName',
    password = '12345',
    database = 'DataBase_Name'
)
cursor = db.cursor()

while True:
    new_task = input(f"{Fore.CYAN}[ Commands ➤ exit: Exit From Program | clear: Clear Terminal | ls: Show Tasks | del [ID]: Delete Task | Write Task and Enter: Add Tasks ]{Style.RESET_ALL}\n{Fore.BLUE}New Task{Style.RESET_ALL} {Fore.YELLOW}➤{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX} ")
    if new_task == "exit":
        break

    elif new_task == "clear":
        os.system("clear")

    elif new_task.startswith("del "):
        try:
            task_id = new_task.split(" ")[1]
            cursor.execute("DELETE FROM list WHERE id = %s", (task_id,))
            db.commit()

            if cursor.rowcount == 0:
                raise Exception(f"ID {task_id} does not exist.")
            
            print(f"{Fore.GREEN}Task {task_id} deleted.{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")


    elif new_task == "ls":
        cursor.execute("SELECT * FROM list")
        res = cursor.fetchall()
        for task in res: 
            print(f"{Fore.MAGENTA}ID ➤ {task[0]} | Description ➤ {task[1]}{Style.RESET_ALL}")

    else:
        cursor.execute("INSERT INTO list (description) VALUES (%s)", [new_task])
        db.commit()
