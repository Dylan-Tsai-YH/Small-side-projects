while True:
    try:
        inp=int(input("""
Welcome to the simple networking operator:
1. Convert IPv4 into binary
2. Find Network Address
3. Exit
""").strip())
        
        if inp == 1: 
            while True:
                try:
                    inp = str(input("\nEnter ip (1 to exit):"))
                    ip = inp.strip().split(".")
                    if inp == "1":
                        print()
                        break
                    elif not(all(int(x) >=0 and int(x)<= 255 for x in ip) and len(ip)==4):
                        print("Invalid input")
                    else:
                        print(".".join(map(lambda x: bin(int(x))[2:].zfill(8), ip)))
                        print()
                except Exception as e:
                    print(f"Error: {e}\n")
                    break 

        elif inp == 2:
            while True:
                try:
                    ip = list(map(lambda x: int(x) ,str(input("\nEnter the ip (Enter 1 to quit): ")).strip().split(".")))
                    if ip[0] == 1 and len(ip)==1:
                        break
                    elif not(all(int(x) >=0 and int(x)<= 255 for x in ip) and len(ip)==4):
                        print("Invalid input")
                        continue
                    
                    netmask = list(map(lambda x: int(x) ,str(input("Enter the network mask: ")).strip().split(".")))
                    if not(all(int(x) >=0 and int(x)<= 255 for x in netmask) and len(netmask)==4):
                        print("Invalid input")
                        continue
                    
                    network = [x&y for (x,y) in zip(ip,netmask)]
                    print(f"\nNetwork Address: {".".join(map(lambda x:str(x), network))}")
                    print(f"Binary: {".".join(map(lambda x:bin(x)[2::].zfill(8),network))}")
                
                except Exception as e:
                    print(f"Error: {e}\n")
                    
        elif inp ==3 :
            print("\nGoodbye")
            break
        
        else:
            print("Invalid input (Only put options 1-3)\n")
    
    except Exception as e:
        print(f"Error: {e}\n")