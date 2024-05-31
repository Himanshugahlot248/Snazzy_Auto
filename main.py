models = {
  'Hatchback': 535000,
  'Saloon': 495000,
  'Estate': 625000
}

optional_extras = {
  'Set of luxury seats': 45000,
  'Satellite navigation': 5500,
  'Parking sensors': 10000,
  'Bluetooth connectivity': 350,
  'Sound system': 1000
}

buyer = {}

while True:
  try:
    print("-------Welcome to Snazzy Autos-------")
    
    # select the model
    print("Select the model you want to buy: ")
    print("MODEL             PRICE")
    for idx, key in enumerate(models):
      print(f"{idx+1}. {key}: \tRs. {models[key] / 100000} lakh")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if 1 <= choice <= 3:
      selected_model = list(models.keys())[choice -1]
      buyer['model'] = selected_model
      buyer['base_price'] = models[selected_model]
      print(f"you selected {selected_model} , with Base Price: Rs. {models[selected_model] / 100000} lakhs")

      # select the optional extras
      print('Select any optional extras you want: ')
      print("OPTIONAL EXTRAS              PRICE")
      for idx, key in enumerate(optional_extras):
        print(f"{idx+1} . {key:<25}: Rs. {optional_extras[key]}")
      print("6 . Finish selection")

      extras_choice =[]
      while True:
        try:
          choice = int(input("Enter your choice of optional extras (1-6): "))
          if 1<= choice <=5:
            selected_extra = list(optional_extras.keys())[choice - 1]
            if (selected_extra in extras_choice):
              print("You have already selected this extra, Please select another one!")
              continue
            extras_choice.append(selected_extra)
            print(f"-------{selected_extra} added, with Price: Rs. {optional_extras[selected_extra]}-------")
          elif choice == 6:
            print(f"You have selected \nModel: {selected_model}\tPrice: Rs. {models[selected_model]}\nOptional Extras: {extras_choice}")
            break
          else:
            print("Invalid choise, please enter value again!")
        except:
          print("Invalid choise, please enter value again!")
          continue
      buyer['Extras'] = extras_choice
      total_price = buyer['base_price']
      for extras in extras_choice:
        total_price += optional_extras[extras] 

      buyer['total_price'] = total_price

      print(f"-------The total Price including all the Extras is: Rs. {total_price} lakhs-------")

      # Trade in old car
      while(True):
        ans = input("Do you have an old car to trade (yes/no): ")
        if ans == 'yes':
          old_car_to_trade = True
          while True:
            try:
              discount_for_old_car = int(input("Enter selling price for your old car(10000 - 100000): "))
              if 10000 <= discount_for_old_car <=100000:
                total_price -= discount_for_old_car
                break
              else:
                print("Enter price Between 10,000 to 1,00,000 !!")
            except:
              print("Enter valid price between 10,000 to 1,00,000 !!")
          print(f"-------Total price after discount is: Rs. {total_price}-------")
          break
        elif ans == 'no':
          old_car_to_trade = False
          discount_for_old_car = total_price * (5/100)
          total_price -= discount_for_old_car
          print(f"-------Total price after discount of 5% is: Rs. {total_price}-------")
          break
        else:
          print("Invalid choice, Please enter either yes or no: ") 
      buyer['old_car_to_trade'] = old_car_to_trade
      buyer['discount_for_old_car'] = discount_for_old_car
      buyer['total_price'] = total_price

      # Repeat Customer
      while True:
        ans = input("Are you a regular customer (yes/no): ")
        if ans == 'yes':
          discount_for_repeat_customer = total_price * (10/100)
          total_price -= discount_for_repeat_customer
          print(f"-------Total Price after discount is: Rs. {total_price}-------")
          break
        elif ans == 'no':
          break
        else:
          print("Enter valid input (yes/no)")
      buyer['total_price'] = total_price

      # Payment method
      while True:
        try:
          print("Select the payment method: ")
          print("1. Pay full Amount now")
          print("2. Equal monthly payments over 4 years (no extra charges)")
          print("3. Equal monthly payments over 7 years, total price increased by 5%")

          ans = int(input("Enter your choice (1-3): "))
          if ans == 1:
            buyer['payment_method'] = "Pay full Amount now"
            # offer on full payment
            try:
              print("Choose one offer:")
              print("\t1. Cashback of 1%\n\t2. Free Optional extra")
              offer_chosen = int(input("Enter your choise (1/2): "))
              if offer_chosen == 1:
                cashback_amount = total_price * (1/100)
                total_price -= cashback_amount
                break
              elif offer_chosen == 2:
                optional_left = [key for key in optional_extras.keys() if key not in extras_choice]
                print("OPTIONAL EXTRAS              PRICE")
                for idx, key in enumerate(optional_left):
                  print(f"{idx+1} . {key:<25}: Rs. {optional_extras[key]}")
                while True:
                  choice = int(input("Enter your choice of optional extras: "))
                  if 1<= choice <=len(optional_left):
                    selected_extra = list(optional_left)[choice - 1]
                    extras_choice.append(selected_extra)
                    print(f"-------You have selected {selected_extra}, with Price: Rs. {optional_extras[selected_extra]} for FREE!-------")
                    break
                  else:
                    print("Invalid choise, please enter value again!")
            except:
              print("Enter valid input (1/2): ")
            break
          elif ans == 2:
            buyer['payment_method'] = "Equal monthly payments over 4 years (no extra charges)"
            break  
          elif ans == 3:
            buyer['payment_method'] = "Equal monthly payments over 7 years, total price increased by 5%"
            increased_amount = total_price * (5/100)
            total_price += increased_amount
            break
          else: 
            print("Enter valid input (1-3): ")
          print(f"-------Your payment method is: {buyer['payment_method']}-------")
        except:
          print("Enter valid input between 1-3!!")
      buyer['total_price'] = total_price
       
      print(f"\nYour order details are: \n")
      for data in buyer:
        print(f"{data :<25} {buyer[data]}")
      break

    elif choice == 4:
      print("Thank You for Visiting!")
      break
    else: 
      print("Invalid choise, please enter value again!")
  except:
    print("Invalid choice, please enter value again!")
    continue