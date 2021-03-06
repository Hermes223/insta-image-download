# main
from insta_image_download import *
import sys

#This is for argument passing for fast checking all pages
#I used this option for fast page checking in my startup
numberOfArguments = len(sys.argv)
if numberOfArguments == 2:
    choice = sys.argv[1]
    if str(choice)=="fast":
        option_two()


menuItems = [
    {"Check one page for new post": option_one},
    {"Check all pages":option_two},
    {"To see images of a page in slide show": option_six},
    {"Add a new page ": option_three},
    {"Delete a page":option_four},
    {"Turn video download on":option_five},
    {"Exit": exit}
]

def main():
    while(True):
        option = Options()
        os.system("clear")
        fig = Figlet(font='doom')
        print(fig.renderText("post download"))
        print("ATTENTION: video download option is off as default!\
            \nif you want to turn it on,first install selenium,\
            \nthen choose option four :)\n")
        for item in menuItems:
            print("[" + str(menuItems.index(item)) + "]" + list(item.keys())[0])

        choice = int(input(">> "))
        list(menuItems[choice].values())[0]()

main()
