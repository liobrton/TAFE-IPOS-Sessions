def main():
    pass

    try:
        # Phase 1: File Navigation
        with open('data.bin', 'rb') as b_file:
            # Navigate to the 5th byte position
            b_file.seek(4)
            print(b_file.tell())
            # Read and print the next 4 bytes from the current position
            print(b_file.read(4).decode('utf-8'))

            # Move the file pointer to the beginning of the file
            b_file.seek(0)
            print(b_file.tell())
            # Read and print the first 8 bytes from the file
            print(b_file.read(8).decode('utf-8'))

            # Print the current file pointer position
            print(b_file.tell())

            # Use the find() method to search for the string "ABC" in the file
            print()




        # Re-open the data.bin file in binary write-append mode

            # Use the tell() method to get the current file pointer position and store it as a bookmark


            # Write the string "XYZ" to the file


            # Use the bookmarked pointer position to append the string "123" to the file

    # create three non-naked exception handlers for:
    # not finding the file, i/o error & all other exceptions
    except FileNotFoundError:
        print('Error: File not found.')

    except IOError:
        print('Error: Unable to open or write to file.')

    except Exception as error:
        print(f'Error: {error}')

if __name__ == "__main__":
    main()
