#  dictionary
hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}


# my functions
def checking_in():
  occupants = input("Yay! And how many will be checking in today? ")
  if int(occupants) <= 6:
    print("Perfect. We can accommodate that.")
    if int(occupants) == 1:
      y = str(input("What is your name? "))
    else:
      y = str(input("What are your names? "))

    print(f"Hello {y}, party of {occupants}! Below is your floor and room number.")
      
    import random

    floor = str(random.randrange(1, 4))
    room = str(random.randrange(10, 41))
    room_number = (floor + room)


    while True:
      try:
        for k in hotel.items():
          if k != room_number:
            print(f"Floor: {floor}")
            print(f"Room Number: {room_number}")
            print("Enjoy your stay at Hotel del Luna.")

            hotel[floor][room_number] = y

            break

        break

      except KeyError:
        break

    new_register = input("Would you like to see the new register? ")
    if new_register == ("yes"):
      print(f"New Register: {hotel}")
    else:
      exit()

  else:
    print("I'm sorry. We can only accommodate parties of less than 6!")


def checking_out():
  room_number = str(input("Excellent. I hope you enjoyed your stay with us. What is your room number? "))

  while True:
    try:
      for k in hotel.items():
        del k[room_number]

        print("Wonderful. Thank you for staying at Hotel del Luna. We hope to see you again!")
        
        new_register = input("Would you like to see the new register? ")

        if new_register == ("yes"):
          print(f"New Register: {hotel}")
        else:
          exit()

    except KeyError:
      break


#THE THANG
check = input("Welcome to Hotel del Luna. Will you be checking in or checking out with us today? ").lower()

if check == ("in"):
  checking_in()

elif check == ("out"):
  checking_out()

else:
  exit()