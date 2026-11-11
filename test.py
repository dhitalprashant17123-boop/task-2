def billing():
    print ("Welcome to the Shopping Mall!")
    
    # Ask for number of items
    n = int(input("How many items do you want to buy:"))
    
    items = []
    total = 0
    
    # Input item names and prices
    try:
        for i in range(1, n+1):
            name = input(f"Enter name of item {i}: ")
            price = float(input(f"Enter price of {name}: Rs "))
            assert price > 0, "Price must be a positive number."
            quantity = int(input(f"Enter quantity of {name}: "))
            assert quantity > 0, "Quantity must be a positive integer."
            
            Amount=price*quantity
            items.append((name, price , quantity,Amount))
            total += Amount
        subtotal=total

        #Ask the customer about the tips    
        tips=float(input("\nEnter tips amount (Rs): "))
        total+=tips

    
        # Print receipt
        print("="*62)
        #to set the alignment of the text in the receipt
        print("{:<15} {:>10} {:>17} {:>17}".format("Item", "Price (Rs)","Quantity","Amount"))
        print("-"*62)

        #Accesing the items list to print the receipt
        for name, price , quantity , Amount in items:
            print("{:<15} {:>8.2f} {:>15} {:>20}".format(name, price ,quantity,Amount))
        print("-"*62)
        print("{:<15} {:>46}".format("Sub Total bill", subtotal))
        print("{:<15} {:>46}".format("Tips", tips))
        print("{:<15} {:>46}".format("Total Bill", total))
        print("="*62)
        
        print("{:>45}".format("Thanks for visiting us !"))
    except AssertionError as e:
                print(f"Error: {e}")
billing()
