import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # Darwin är macOS
        os.system("sudo shutdown -h now")
    else:
        print("Operativsystemet stöds inte")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("sudo shutdown -r now")
    else:
        print("Operativsystemet stöds inte")

# Använd shutdown() för att stänga av datorn eller restart() för att starta om den
restart()  # eller shutdown()