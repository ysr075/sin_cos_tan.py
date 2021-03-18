#!/usr/bin/python3

import os
import time

def main():
    choice = float(input("""
        ╔═════════════════════╗
        ╠   coded by @ysr075  ╣
        ╚═════════════════════╝
           ╔═══════════════╗
           ║ ╔═══════════╗ ║
           ║ ╠   1.sin   ╣ ║
           ║ ╠   2.cos   ╣ ║
           ║ ╠   3.tan   ╣ ║
           ║ ╚═══════════╝ ║
           ╚═══════════════╝
        ╔═════════════════════╗
                input: """))
    while True:
        if choice ==  1:
            # sin
            os.system("cls")
            sin_a_b = float(input("""
        ╔═════════════════════╗
        ╠   coded by @ysr075  ╣
        ╚═════════════════════╝
           ╔═══════════════╗
           ║ ╔═══════════╗ ║
           ║ ╠    1.α    ╣ ║
           ║ ╠    2.β    ╣ ║
           ║ ╠  3.return ╣ ║
           ║ ╚═══════════╝ ║
           ╚═══════════════╝
        ╔═════════════════════╗
                input: """))
            if sin_a_b == 1:
                print("        ╚═════════════════════╝")
                BC = float(input("|BC| = "))
                AB = float(input("|AB| = "))
                alpha = (BC/AB)
                print("\nα:", alpha, "°\n")
                seconds = int(5)
                for i in range(seconds):
                  print(str(seconds - i))
                  time.sleep(1)
                os.system("cls")
                return main()
            elif sin_a_b == 2:
                print("        ╚═════════════════════╝")
                AC = float(input("|AC| = "))
                AB = float(input("|AB| = "))
                beta = (AC/AB)
                print("\nβ:", beta, "°\n")
                seconds = int(5)
                for i in range(seconds):
                  print(str(seconds - i))
                  time.sleep(1)
                os.system("cls")
                return main()
            else:
                os.system("cls")
                return main()
# --------------------------------------------------------------------------------------
        elif choice == 2:
            # cos
            os.system("cls")
            sin_a_b = float(input("""
        ╔═════════════════════╗
        ╠   coded by @ysr075  ╣
        ╚═════════════════════╝
           ╔═══════════════╗
           ║ ╔═══════════╗ ║
           ║ ╠    1.α    ╣ ║
           ║ ╠    2.β    ╣ ║
           ║ ╠  3.return ╣ ║
           ║ ╚═══════════╝ ║
           ╚═══════════════╝
        ╔═════════════════════╗
                input: """))
            if sin_a_b == 1:
                print("        ╚═════════════════════╝")
                AC = float(input("|AC| = "))
                AB = float(input("|AB| = "))
                alpha = (AC/AB)
                print("\nα:", alpha, "°\n")
                seconds = int(5)
                for i in range(seconds):
                  print(str(seconds - i))
                  time.sleep(1)
                os.system("cls")
                return main()
            elif sin_a_b == 2:
                print("        ╚═════════════════════╝")
                BC = float(input("|BC| = "))
                AB = float(input("|AB| = "))
                beta = (BC/AB)
                print("\nβ:", beta, "°\n")
                seconds = int(5)
                for i in range(seconds):
                  print(str(seconds - i))
                  time.sleep(1)
                os.system("cls")
                return main()
            else:
                os.system("cls")
                return main()
# --------------------------------------------------------------------------------------
        elif choice == 3:
            # tan
            os.system("cls")
            sin_a_b = float(input("""
        ╔═════════════════════╗
        ╠   coded by @ysr075  ╣
        ╚═════════════════════╝
           ╔═══════════════╗
           ║ ╔═══════════╗ ║
           ║ ╠    1.α    ╣ ║
           ║ ╠    2.β    ╣ ║
           ║ ╠  3.return ╣ ║
           ║ ╚═══════════╝ ║
           ╚═══════════════╝
        ╔═════════════════════╗
                input: """))
            if sin_a_b == 1:
                print("        ╚═════════════════════╝")
                BC = float(input("|BC| = "))
                AC = float(input("|AC| = "))
                alpha = (BC/AC)
                print("\nα:", alpha, "°\n")
                seconds = int(5)
                for i in range(seconds):
                  print(str(seconds - i))
                  time.sleep(1)
                os.system("cls")
                return main()
            elif sin_a_b == 2:
                print("        ╚═════════════════════╝")
                AC = float(input("|AC| = "))
                BC = float(input("|BC| = "))
                beta = (AC/BC)
                print("\nβ:", beta, "°\n")
                seconds = int(5)
                for i in range(seconds):
                  print(str(seconds - i))
                  time.sleep(1)
                os.system("cls")
                return main()
            else:
                os.system("cls")
                return main()
        else:
          os.system("cls")
          return main();
main()
