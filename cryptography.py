alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

def menu():
    print("SECRET DECODER MENU\n")
    print("0) Quit")
    print("1) Encode")
    print("2) Decode\n")
    response = input("What do you want to do?")             #getting user's input and storing in a variable
    return response                                         #returning response for later use

def encode(plain):
    encodedString = ""                                      #creating an empty string
    for letter in plain.upper():                            #for loop begins for plain
        if letter in alpha:
            position = alpha.index(letter)                  #getting an integer and storing in a variable
            encode = key[position]                          #assigning that specific integer to a letter in key
            encodedString = encodedString + encode          #concatenate both values
    return encodedString                                    #returning encodedString

def decode(coded):
    decodedString = ""
    for letter in coded.upper():
        if letter in key:
            position = key.index(letter)                    #happening everything same as encode function
            decode = alpha[position]                        #but in reverse order
            decodedString = decodedString + decode
    return decodedString

def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = input("text to be encoded: ")
      print(encode(plain))
    elif response == "2":
      coded = input("code to be decyphered: ")
      print(decode(coded))
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    else:
      print ("I don't know what you want to do...")
main()

