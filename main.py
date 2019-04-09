# main
from insta_image_download import *

menuItems = [
    {"Check one page for new post": option_one},
    {"Add a new page ": option_two},
    {"Delete a page":option_three},
    {"Exit": exit}
]

def main():
    option = Options()
    os.system("clear")
    fig = Figlet(font='doom')
    print(fig.renderText("post download"))

    for item in menuItems:
        print("[" + str(menuItems.index(item)) + "]" + list(item.keys())[0])

    choice = int(input(">> "))
    list(menuItems[choice].values())[0]()

main()	