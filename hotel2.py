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
        for k in hotel.values():
          if k != room_number:
            print(f"Floor: {floor}")
            print(f"Room Number: {room_number}")
            print("Enjoy your stay at Hotel del Luna.")

            hotel[floor][room_number] = y

        break

      except KeyError:
        break

    print(f"New Register: {hotel}")

  else:
    print("I'm sorry. We can only accommodate parties of less than 6!")

  
def checking_out():
  room_number = str(input("Excellent. I hope you enjoyed your stay with us. What is your room number? "))

  while True:
    try:
      for k in hotel.values():
        del k[room_number]

        print(f"New Register: {hotel}")

        print("Wonderful. Thank you for staying at Hotel del Luna. We hope to see you again!")

    except KeyError:
      break



check = input("Welcome to Hotel del Luna. Will you be checking in or checking out with us today? ")

if check == ("checking in"):
  checking_in()

elif check == ("checking out"):
  checking_out()

else:
  exit()