# Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal

def text_to_bytes(text):
    return text.encode('utf-8')

def bytes_to_text(bytes):
    return bytes.decode('utf-8')

def byte_reversal(bytes):
    return bytes[::-1]

# Main program logic
try:
    # Open the binary file for reading and create output text and bytes files for writing using the context manager
    with (open('data.bin', 'br') as file,
          open('reversed_bytes.bin', 'wb') as b_file,
          open('converted_text.txt', 'a') as t_file):
        # Iterate through each line in the binary file
        for line in file:
            # Decode the line to Unicode string and remove leading/trailing whitespaces
            line = line.decode('utf-8').strip()

            # Check if the line starts with "TEXT:"
            if line.startswith("TEXT:"):
                # Extract text content, convert to uppercase, and write to text file
                text = line[len("TEXT:"):].upper()
                t_file.write(text)

            # Check if the line starts with "BYTES:"
            elif line.startswith("BYTES:"):
                ...
                # Extract the string and encode to hexadecimal
                string = line[len('BYTES:'):]
                encoded_hex = string.encode().hex()
                ...
                # Extract byte content, convert to bytes object(using fromhex()),
                byte_content = bytes.fromhex(encoded_hex)

                # reverse bytes, and write to bytes file
                reversed_bytes = byte_reversal(byte_content)
                b_file.write(reversed_bytes)

    # Print success message
    print("Conversion completed successfully.")

# Handle file I/O errors
except IOError:
    print('Error: Unable to open or write to file.')

# Handle other exceptions using the exception class
except Exception as error:
    print(f'Error: {error}')

