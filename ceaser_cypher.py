print(''' welcome to ceaser cypher  ______                                                            ______   __            __                           
 /      \                                                          /      \ |  \          |  \                          
|  $$$$$$\  ______    ______    _______   ______    ______        |  $$$$$$\ \$$  ______  | $$____    ______    ______  
| $$   \$$ |      \  /      \  /       \ |      \  /      \       | $$   \$$|  \ /      \ | $$    \  /      \  /      \ 
| $$        \$$$$$$\|  $$$$$$\|  $$$$$$$  \$$$$$$\|  $$$$$$\      | $$      | $$|  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\
| $$   __  /      $$| $$    $$ \$$    \  /      $$| $$   \$$      | $$   __ | $$| $$  | $$| $$  | $$| $$    $$| $$   \$$
| $$__/  \|  $$$$$$$| $$$$$$$$ _\$$$$$$\|  $$$$$$$| $$            | $$__/  \| $$| $$__/ $$| $$  | $$| $$$$$$$$| $$      
 \$$    $$ \$$    $$ \$$     \|       $$ \$$    $$| $$             \$$    $$| $$| $$    $$| $$  | $$ \$$     \| $$      
  \$$$$$$   \$$$$$$$  \$$$$$$$ \$$$$$$$   \$$$$$$$ \$$              \$$$$$$  \$$| $$$$$$$  \$$   \$$  \$$$$$$$ \$$      
                                                                                | $$                                    
                                                                                | $$                                    
                                                                                 \$$   ''')
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("type 'encode' if you want to encrypt and type 'decode' if you want to decrypt\n").lower()
text=input("enter the word you want to encode or decode\n").lower()
shift=int(input("enter the number by which you want to shift the letters\n"))

def encrypt(original_text,shifted_number):
    cypher_text=""
    for letter in original_text:
        if letter not in alphabets:
            cypher_text+=letter
        else:    
            shifted_position=(alphabets.index(letter) +shifted_number)%26
            new_letter=alphabets[shifted_position]
            cypher_text+=new_letter
    print(f"the encoded word is {cypher_text}")
def decrypt (original_text,shifted_number):
    cypher_text=""
    for letter in original_text:
         if letter not in alphabets:
            cypher_text+=letter
         else:   
            shifted_position=(alphabets.index(letter) -shifted_number)%26
            new_letter=alphabets[shifted_position]
            cypher_text+=new_letter
    print(f"the decoded word is {cypher_text}")



if direction=="encode":
    encrypt(original_text=text,shifted_number=shift)
elif direction=="decode":
    decrypt(original_text=text,shifted_number=shift)

