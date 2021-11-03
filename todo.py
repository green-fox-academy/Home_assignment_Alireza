import customArgumentParser
import datetime
import os
import sys


def getdate():
    return datetime.datetime.now()


z = getdate()
total = 0


class Items(object):
    """
        List stored as a file in ~/.todo
    """

    x = os.getcwd()
    FILE_LOCATION = fr"{x}\todo.txt"
    Done_Location = fr"{x}\done.txt"

    def __init__(self):
        self.items = open(self.FILE_LOCATION, "r").readlines()

    def listAdd(self, arg):
        try:
            print("Added item: " + arg)
            with open(self.FILE_LOCATION, "a+") as f:
                f.writelines(arg + "\n")
        except Exception as e:
            print(f"Error: Unable to add, no {arg} task provided.")

    def listshow(self):
        print("\n                       TODO\n" + "=" * 50)

        if not self.items:
            print("""
Command line arguments:
    --ls       Lists all the tasks
    --add      Adds a new task
    --delete   Removes an task
    --report   report about tasks
    --done     Completes an task\n
    ==========================
    No todos for today! :)\n""")
        else:
            for sno, item in enumerate(self.items):
                print(str(sno + 1) + ". " + item)

    def listDelete(self, arg):

        try:
            doneTask = self.items.pop(arg - 1)

            print("Completed task no. " + str(arg) + " (%s), deleted todo" % doneTask.strip())
            print(f"Deleted item: {arg}")

            with open(self.FILE_LOCATION, "w") as f:
                for item in self.items:
                    f.writelines(item)
        except Exception as e:
            print(f"Error: Unable to remove: no index provided.")

    def listdone(self, arg):

        try:

            g = self.items[arg - 1]
            print(f"Marked todo {arg} as done")

            with open(self.Done_Location, 'a') as f:
                f.write(f"x {z} {g} ")
            doneTask = self.items.pop(arg - 1)

            with open(self.FILE_LOCATION, "w") as f:
                for item in self.items:
                    f.writelines(item)
        except Exception as e:
            print(f"Error: todo {arg} does not exist.")

    def report(self):
        with open(self.Done_Location, "r") as f:
            counter=-1
            content = f.read()
            coList = content.split("\n")
            for i in coList:
                if i:
                    counter+=1

        print(f"{z}    pending: {len(self.items)}  completed: {counter}")


if __name__ == "__main__":
    description = "Todo, for when you need to do."
    parser = customArgumentParser.ArgumentParser(description=description)

    parser.add_argument("--add", type=str, help=" # Add a new todo")
    parser.add_argument("--report", action="store_true", help="# report item")
    parser.add_argument("--ls", action="store_true", help="# Show remaining todos")
    parser.add_argument("--delete", type=int, help="# Delete a todo")
    parser.add_argument("--done", type=int, help="# Complete a todo")

    args = parser.parse_args()

    items = Items()
    if not (args.add or args.ls or args.delete or args.report or args.done):
        items.listshow()

    elif args.add:
        # print("calling items.listAdd")
        items.listAdd(args.add)

    elif args.ls:
        items.listshow()

    elif args.delete:
        items.listDelete(args.delete)

    elif args.done:
        items.listdone(args.done)

    elif args.report:
        items.report()
