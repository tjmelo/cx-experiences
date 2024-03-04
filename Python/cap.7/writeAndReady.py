print("Start program")

# Writing file

isFile = './cap.7/files/Example1.txt'

recordingText = "Writing and read text file"
fileToWrite = open(isFile, 'w')
fileToWrite.write(recordingText)
fileToWrite.close()

# Reading file

fileToWrite = open(isFile, 'r')
fileToRead = fileToWrite.readline()
fileToWrite.close()

print("String readed {}".format(fileToRead))
