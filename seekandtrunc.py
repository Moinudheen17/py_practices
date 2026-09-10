sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)
with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
      
  
  file.seek(0)
  unsent_message = 'This message has been unsent.'
  file.truncate(len(unsent_message))
print("og message : ",original_message)
print("unsended message : " ,unsent_message)