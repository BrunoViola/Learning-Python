def main():
   sent_message = "Hey there! This is a secret message."

   with open("sent_message.txt", "w") as file:
      file.write(sent_message)
   
   with open("sent_message.txt", "r+") as file:
      original_message = file.read()
      file.seek(0) # Move the cursor to the beginning of the file

      unset_message = "This message has been unset." # Modify the message to simulate unsending
      file.truncate(len(unset_message)) # Truncate the file to the length of the modified message
      file.write(unset_message)

      print(f'Original message: {original_message}')


if __name__ == "__main__":
   main()