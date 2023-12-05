from pypdf import PdfReader, PdfWriter

reader = PdfReader("C++.encr.pdf")
writer = PdfWriter()


# Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Add a password to the new PDF
# writer.encrypt("armstrong", algorithm="AES-256")

# # Save the new PDF to a file
# with open("C++.encr.pdf", "wb") as f:
#     writer.write(f)


words_dict = open('./dictionary.txt', 'r')

all_words = words_dict.readlines()

# to remove all the newline characters from the words uncomment this
# all_words = [x.strip('\n') for x in words_dict.readlines()]

# print(all_words)
pwd = ''
# arrow
for word in all_words:
    u_case = reader.decrypt(word.strip('\n'))
    print(f"trying {word}...", u_case)
    if u_case > 0:
        pwd = word
        print(f"the password for the pdf file is {word}")
        break
    l_case = reader.decrypt(word.lower().strip('\n'))
    print(f"trying {word.lower()}...", l_case)
    if l_case > 0:
        pwd = word
        print(f"the password for the pdf file is {word.lower()}")
        break

if pwd == '':
    print("could not decrypt password")

print("Done")