# Open the file in read mode

file_read = open('Codingal.txt', 'r')

# Print a message to indicate read mode

print("File in Read Mode -")

# Read and display the content of the file

print(file_read.read())

# Close the file after reading

file_read.close()

# Open the file in write mode (this will overwrite existing content)

file_write = open('Codingal.txt', 'w')

# Print a message to indicate write mode

print("File in Write Mode ....")

# Write content into the file

file_write.write("Hi! I am Penguin. I am 1 yr. old")

# Close the file after writing

file_write.close()

# Open the file in append mode (adds content at the end)

file_append = open('Codingal.txt', 'a')

# Print a message to indicate append mode

print("\nFile in Append Mode ....")

# Append content to the file

file_append.write("\nHi! I am Penguin. I am 1 yr. old")

# Close the file after appending

file_append.close()
