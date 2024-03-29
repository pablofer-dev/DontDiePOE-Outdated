from time import sleep
from ctypes import *
import os
from pymem import *
from pymem.process import *
from sys import stdout
import Conexion as interop
import pyautogui
import asyncio

def Bienvenida():
    print("""\033[;31m"""+"""

    ▓█████▄  ▒█████   ███▄    █ ▄▄▄█████▓   ▓█████▄  ██▓▓█████     ██▓███   ▒█████  ▓█████
    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒   ▒██▀ ██▌▓██▒▓█   ▀    ▓██░  ██▒▒██▒  ██▒▓█   ▀
    ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒ ▓██░ ▒░   ░██   █▌▒██▒▒███      ▓██░ ██▓▒▒██░  ██▒▒███
    ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒░ ▓██▓ ░    ░▓█▄   ▌░██░▒▓█  ▄    ▒██▄█▓▒ ▒▒██   ██░▒▓█  ▄
    ░▒████▓ ░ ████▓▒░▒██░   ▓██░  ▒██▒ ░    ░▒████▓ ░██░░▒████▒   ▒██▒ ░  ░░ ████▓▒░░▒████▒
     ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒   ▒ ░░       ▒▒▓  ▒ ░▓  ░░ ▒░ ░   ▒▓▒░ ░  ░░ ▒░▒░▒░ ░░ ▒░ ░
     ░ ▒  ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░    ░        ░ ▒  ▒  ▒ ░ ░ ░  ░   ░▒ ░       ░ ▒ ▒░  ░ ░  ░
     ░ ░  ░ ░ ░ ░ ▒     ░   ░ ░   ░          ░ ░  ░  ▒ ░   ░      ░░       ░ ░ ░ ▒     ░
       ░        ░ ░           ░                ░     ░     ░  ░                ░ ░     ░  ░
     ░                                       ░
                                       ░
                                       \033[;0m SUPPORT: FER#9919""""\033[;0m \n """)


try:
    Bienvenida()
except:
    print("Error 1004")
os.system("cls")

''' LIFE '''


def GetPointer(pm, base, offsets):
    addr = pm.read_longlong(base + 0x02C7B258)
    for offset in offsets:
        if offset != offsets[-1]:
            try:
                cont = 12
                addr = pm.read_longlong(addr + offset)
            except:
                return False
    return addr


def GetPointer2(pm, base, offsets):
    addr = pm.read_longlong(base + 0x02C7B258)
    for offset in offsets:
        if offset != offsets[-1]:
            try:
                cont = 12
                addr = pm.read_longlong(addr + offset)
            except:
                return False
    return addr


def GetPointer3(pm, base, offsets):
    addr = pm.read_longlong(base + 0x02C7B258)
    for offset in offsets:
        if offset != offsets[-1]:
            try:
                cont = 12
                addr = pm.read_longlong(addr + offset)
            except:
                return False
    return addr

def main():
    try:

        lecturadevida = 0
        # trackvida
        offsets = [0x50, 0x580]
        offsetvida = (0x580)  # offset
        # vidainicial poe
        offsets2 = [0x50,0x578]
        offsetvida2 = (0x578)  # offset

        # manatrack
        offsets3 = [0x88,0xB80]
        offsetmana3 = (0xB80)  # offset

        # manainicial
        offsets4 = [0x50,0xB78]
        offsetmana4 = (0xB78)  # offset

        string = str(interop.get_process_name(
            (interop.find_process(b'PathOfExile'))))
        characters = "b'"
        game = ''.join(x for x in string if x not in characters)
        pm = pymem.Pymem(game)
        gameModule = module_from_name(
            pm.process_handle, game).lpBaseOfDll

        if type(GetPointer(pm, gameModule, offsets)) is int:
            vida = GetPointer(pm, gameModule, offsets)
            vida2 = GetPointer(pm, gameModule, offsets2)
            mana = GetPointer2(pm, gameModule, offsets3)
            manaI = GetPointer3(pm, gameModule, offsets4)
            union4 = manaI + offsetmana4
            union3 = mana + offsetmana3
            union2 = vida2 + offsetvida2
            union = vida + offsetvida
            os.system("cls")
            lecturadevidaInicial = pm.read_int(union2)
            lecturademanaInicial = pm.read_int(union4)

        elif GetPointer(pm, gameModule, offsets) == False or lecturadevidaInicial < 0:
            os.system("cls")
            print("\033[;31m" + "Start the game")
            sleep(9)
            return

        Bienvenida()
        while True:
            contador = 0
            lecturademanaInicial = pm.read_int(union4)
            lecturademana = pm.read_int(union3)
            lecturadevida = pm.read_int(union)
            vidaFinal = (40 * lecturadevidaInicial) / 100
            vidaPot = (60 * lecturadevidaInicial) / 100
            lecturadevidaInicial = pm.read_int(union2)
            stdout.write("\r" + "               Inicial Life: " +
                         str(lecturadevidaInicial) + "   Life: " + str(lecturadevida) + "   Inicial Mana: " + str(lecturademanaInicial) + "   Mana : " + str(lecturademana))

            stdout.flush()

            if lecturadevida <= vidaFinal:
                interop.kill_connection(interop.find_process(b'PathOfExile'))
                break
            elif lecturadevida <= vidaPot and lecturadevida < (lecturadevidaInicial - ((30 * lecturadevidaInicial)/100)):
                pyautogui.press("1")
                break
            elif lecturademana <= lecturademanaInicial and lecturademana <= (lecturademanaInicial - ((30 * lecturademanaInicial)/100)):
                if contador == 0:
                    pyautogui.press("5")
                    contador+=1
                    break
                elif contador >= 1:
                    contador+=1
                    if contador == 300:
                        contador=0
                    break
                        
                break

    except Exception as e:
        print(e)


    
while True:
    main()
