# Python File Write

# ExampleGet your own Python Server
# Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# Example
# Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

# Note: the "w" method will overwrite the entire file.

f = open("myfile.txt", "x")
f = open("myfile.txt", "w")