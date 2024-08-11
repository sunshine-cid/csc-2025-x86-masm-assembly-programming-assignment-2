# Student Name
# CSC 2025 - XXX - Computer Arch/Assembly Language
# Binary/Hex/Integer Conversion
# Date
# Python 3.12.1
# Prompt the user to input a 16-bit Binary value, 32-bit Hexadecimal value, or Integer value then converts to and displays the other two.

# hexCharToInt
# Function Name: hexCharToInt
# Inputs: Recieves a Hex Char
# Outputs: Returns an Int
# Memory Usage: 23.469MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Simplifies the repeated process of converting a hex character to an integer value
def hexCharToInt(input):
    if (input >= '0') and ( input <='9'):
        return ord(input) - ord('0')
    elif (input.lower() >= 'a') and (input.lower() <= 'f'):
        return ord(input.lower()) - ord('a') + 10
    else:
        raise ValueError("Invalid Hex Value:", input)

# Function Name: signed16bitBinaryInput
# Inputs: No values passed. Takes input string from User
# Outputs: No values returned. Displays values returned from binToHex and binToInt functions
# Memory Usage: 23.504MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Used to recieve binary input value and displays converted results.
def signed16bitBinaryInput():
    binaryInput = ""
    binaryInput = input("Please enter the signed 16-bit binary value:")
    try:
        print("Hexadecimal value:", binToHex(binaryInput))
        print("Integer value:", binToInt(binaryInput))
    except:
        print("Error: Invalid input")

# Function Name: signed32bitHexInput
# Inputs: No values passed. Takes input string from user
# Outputs: No value returned. Displays values returned from hexToBin and hexToInt
# Memory Usage: 23.469MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Used to recieve hex input value and displays converted results.
def signed32bitHexInput():
    hexInput = ""
    hexInput = input("Please enter the signed 32-bit hex value:")
    try:
        print("Binary value:", hexToBin(hexInput))
        print("Integer value:", hexToInt(hexInput))
    except:
        print("Error: Invalid input")

# Function Name: signedIntInput
# Inputs: No values passed. Takes input string from user
# Outputs: No value returned. Displays values returned from intToBin and intToHex
# Memory Usage: 23.461MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Used to recieve integer input value and displays converted results.
def signedIntInput():
    intInput = ""
    intInput = input("Please enter the signed integer value:")
    try:
        print("Binary value:", intToBin(intInput))
        print("Hex value:", intToHex(intInput))
    except:
        print("Error: Invalid input")

# Function Name: binToHex
# Inputs: Is passed a binary value as a string
# Outputs: Returns a hex valu4e as a string
# Memory Usage: 23.504 MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Utilizes two other functions (binToInt and intToHex) to convert a binary string to a hex string
def binToHex(input):
    return intToHex(binToInt(input))

# Function Name: 
# Inputs: Is passed a hex value as a string 
# Outputs: Returns a binary value as a string
# Memory Usage: 23.469MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Utilizes two other functions (hexToInt and intToBin) to convert a hex string to a binary string
def hexToBin(input):
    return intToBin(hexToInt(input))
    
# Function Name: binToInt
# Inputs: Is passed a binary vlaue as a string for input
# Outputs: Returns a signed integer
# Memory Usage: 23.504MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Accepts a signed binary value as a string, converts to integer, does two's complement if negative.
def binToInt(input):
    intToReturn = 0
    # Checking to see if the input is signed negative, if it is invert and return negative
    if input[0] == '1':
        invertedInput = 0
        # Apply the two's complement to get the negative value with error checking
        for char in input:
            invertedInput = invertedInput * 2
            if char == '0':
                invertedInput += 1
            elif char =='1':
                invertedInput += 0
            else:
                raise ValueError("Invalid Binary Value:", char)
        invertedInput += 1
        intToReturn = -invertedInput
    # Otherwise our value is positive, convert with error checking
    else:
        for char in input:
            intToReturn = intToReturn * 2 
            if char == '1':
                intToReturn += 1
            elif char == '0':
                intToReturn += 0
            else:
                raise ValueError("Invalid Binary Value:", char)
    return intToReturn

# Function Name: hexToInt
# Inputs: Is passed a hex value as a string 
# Outputs: Returns an signed integer
# Memory Usage: 375.5MiB  **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: 
def hexToInt(input):
    intToReturn = 0
    # Remove 0x or 0X if present
    if input.startswith('0x') or input.startswith('0X'):
        input = input[2:]
    
    # If the int value of the first character >=8 the signed muber is negative
    # Apply the two's complement, and return the negative value
    if hexCharToInt(input[0]) >= 8:
        invertedInput = 0
        for char in input:
            invertedInput = invertedInput * 16 + (15 - hexCharToInt(char)) 
        invertedInput += 1
        intToReturn = -invertedInput
    # Otherwise conmvert the positive number to int
    else:
        for char in input:
            intToReturn = intToReturn * 16 + hexCharToInt(char)

    return intToReturn

# Function Name: intToBin
# Inputs: Is passed a signed intetger as a string as input
# Outputs: Returns a 16-bit signed binary as a string
# Memory Usage: 23.469MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Checks if input is 0, converts the absolute integer value to binary, if the input was signed as negative applys two's complement
def intToBin(input):  
    # Catch for if the value is 0, just return "0"
    if int(input) == 0:
        return "0".zfill(16)
    
    binStrToReturn = ""
    tempInput = abs(int(input))

    # Conver tempInput value to binary string
    while tempInput > 0:
        binStrToReturn = str(tempInput % 2) + binStrToReturn
        tempInput = tempInput // 2    
    
    binStrToReturn = binStrToReturn.zfill(16)

    # If the input number is negative apply two's compliment
    if (int(input) < 0):
        tempBinStrToReturn = ''
        for bit in binStrToReturn:
            if bit == '0':
                tempBinStrToReturn = tempBinStrToReturn + "1"
            elif bit == '1':
                tempBinStrToReturn = tempBinStrToReturn + "0"
            else:
                raise ValueError("Invalid Binary Bit:", bit)
        # Add 1 and carry up the inverted binary string
        carryInt = 1
        complementBinStr = ''
        for bit in reversed(tempBinStrToReturn):
            if bit == '1' and carryInt == 1:
                complementBinStr = '0' + complementBinStr
            elif bit == '0' and carryInt == 1:
                complementBinStr = '1' + complementBinStr
                carryInt = 0
            else:
                complementBinStr = bit + complementBinStr
        binStrToReturn = complementBinStr
    return binStrToReturn
            
# Function Name: intToHex
# Inputs: Is passed a signed integer as a string
# Outputs: Returns a signed 32-bit hex as string
# Memory Usage: 23.504MiB **This is total memory usage as read by a memory profiler when this function was executing.
# Operational Description: Check for case 0, determines absolute value, converts to hex, if original input was signed negative applys two's complement
def intToHex(input):
    # Address 0 case with simple and quick return
    if int(input) == 0:
        return "0x00000000"
    
    hexStrToReturn = ""
    tempInput = abs(int(input))

    # Convert absolute value to hex
    while tempInput > 0:
        remainderInt = tempInput % 16
        if remainderInt < 10:
            hexStrToReturn = chr(remainderInt + ord('0')) + hexStrToReturn
        else:
            hexStrToReturn = chr(remainderInt - 10 + ord('A')) + hexStrToReturn
        tempInput = tempInput // 16

    # Add digits to pad result to 32nits
    hexStrToReturn = hexStrToReturn.zfill(8)

    # If the number is a negative, apply two's compliment
    if int(input) < 0:
        tempHexStrToReturn = ""
        # Build two's complement in tempHexStringToReturn 
        for char in hexStrToReturn:
            if char >= '0' and char <= '9':
                tempDigit = 15 - int(char)
            else:
                tempDigit = 15 - (ord(char) - ord('A') + 10)
            if tempDigit < 10:
                tempHexStrToReturn = tempHexStrToReturn + chr(tempDigit + ord('0'))
            else:
                tempHexStrToReturn = tempHexStrToReturn + chr(tempDigit - 10 + ord('A'))
        # Add 1 and carry if necessary
        carryInt = 1
        complementHexStr = ""
        for char in reversed(tempHexStrToReturn):
            if char >= '0' and char <= '9':
                total = int(char) + carryInt
            else:
                total = (ord(char) - ord('A') + 10) + carryInt

            if total >= 16:
                complementHexStr = '0' + complementHexStr
                carryInt = 1
            else:
                if total < 10:
                    complementHexStr = chr(total + ord('0')) + complementHexStr
                else:
                    complementHexStr = chr(total - 10 + ord('A')) + complementHexStr
                carryInt = 0
                
        hexStrToReturn = complementHexStr

    return "0x" + hexStrToReturn

# Initialize some variables
menuSelection = ''

# Program entry point
if __name__ == "__main__":
    # This while loops displays the menu and takes user input for the menu selection
    while True:
        print("This program takes in a signed 16-bit Binary, signed 32-bit Hexadecimal, or Integer value and then coverts to and displays the other two.")
        print("Please select from the menu (i.e. 1):")
        print("1. Signed 16-bit Binary value")
        print("2. Signed 32-bit Hexadecimal value")
        print("3. Integer value")
        print("4. Quit")
        
        menuSelection = input()

        if (menuSelection == '1'):
            signed16bitBinaryInput()
        elif (menuSelection == '2'):
            signed32bitHexInput()
        elif (menuSelection == '3'):
            signedIntInput()
        elif (menuSelection == '4'):
            print("Thank you for running this program. Quitting...")
            break
        else:    
            print("Invalid Selection. Try Again?")
            continue
