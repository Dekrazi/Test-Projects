from controller import add, subtract, multiply, divide


def main():


    calc_menu = {
                1: "Add",
                2: "Subtract",
                3: "Multiply", 
                4: "Divide",
                5: "Exit"
                
        }



    while True:
            print("\n*** MENU ***\n")        
            for key, value in calc_menu.items():
                print(key, value)
            choice = input("What do you want to do? ")
            if choice in ("1", "2", "3", "4",):
                try:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter a number. ")
                    continue
                
            if choice == "1":
                print(x, "+", y, "=", add(x, y))
            if choice == "2":
                print(x, "-", y, "=", subtract(x, y))
            if choice == "3":
                print(x, "8", y, "=", multiply(x, y))
            if choice == "4":
                print(x, "/", y, "=", divide(x, y))
            if choice == "5":
                print("Thanks for using my calculator!")
                break

            
            
        

    

if __name__ == "__main__":
         main()
