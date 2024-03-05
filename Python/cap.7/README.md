Files
=

Files are useful for storing permanent data. When some data is read or written, by a programming language, behind the scenes, what happens is the use of the user's SO resources to make the operations.

In Python, there are two ways to interpret the files: binary mode and text mode.

#### Text files
The format text file when read it's decoded and interpreted accordingly in a specific table of characters. The result of this is returned as a string object.

The writing operation makes an inverse process. The characters are encoded turned in bytes and written on disc.

#### Binary files
The binary files when handled, are translated to the memory without interpretation or decoding. They arrive in a raw mode and it's necessary to implement the resources to interpret them.

## Writing and reading a file in Python
Simple example of how to write and read a file in Python:

```py
isFile = 'Example.txt'

# Writing file
isRecordingText = "Writing and read text file"
fileToWrite = open(isFile, 'w')
fileToWrite.write(isRecordingText)
fileToWrite.close()

# Reading file
fileToRead = open(isFile, 'r')
isRead = fileToRead.readline()
fileToRead.close()
```

### Params of the method .open()

#### file

```py
someFile = open('NameOfFile.txt') # default to 'r' mode
```
Defines the name of the file that will be open.

#### mode

The well knows modes are:
`r`, `r +`, `w`, `w+`, `a`, `a+`, `x`, `x+` 

```py
someFile = open('NameOfFile.txt', 'r')
```

#### buffering

Defines the bufferizing character of the file. The options are: 
- `0`  Do not use a buffer (Only binary files). 
- `1` The file will have a line of file (Only text files)
- `2` `3` `4` `...` Buffer with fixed size
- `-1` Default scheme of buffer

```py
someFile = open('NameOfFile.txt', 'r', -1)
```

#### encoding

Defines the type of codification to the file

```py
someFile = open('NameOfFile.txt', 'r', "utf-8")
```

## Methods to manipulate files
|  Method | Description  |
|---|---|
|`close()`| Close the file opened with `open`|
|`flush()`| Flush the buffer opened to write|
|`read()`|Read all file and return only one string|
|`readline()`|Read the line of file return only one string|
|`readlines()`|Read all line of file return a list of strings|
|`write(string)`|Write in the file a character string|
|`writeLines(list)`|Write in the file all strings in the list|
|`seek(character)`|Change the position of cursor with reference of character|

---
Have a nice code :fire:
