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
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type 'encode' to encrypt and 'decode' to decrypt\n").lower()
text=input(f"enter text to {direction}\n").lower()
shift=int(input("enter the number by which the text is to be shifted\n"))
def encrypt(original_text,shift_amount):
    cipher_text=""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text+=letter
        else:
             shifted_position=alphabet.index(letter) + shift_amount
             shifted_position %= len(alphabet)
             cipher_text+=alphabet[shifted_position]
    print(f"here is the encoded result:{cipher_text}")   
   
def decrypt(original_text,shift_amount):
     cipher_text=""
     for letter in original_text:
        if letter not in alphabet:
            cipher_text+=letter
        else:
            shifted_position=alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            cipher_text+=alphabet[shifted_position]
     print(f"here is the decoded result:{cipher_text}")
if direction=="encode":
    encrypt(original_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(original_text=text,shift_amount=shift)
continue1=True
while continue1:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text=input(f"enter text to {direction}\n").lower()
    shift=int(input("enter the number by which the text is to be shifted\n"))
    if direction=="encode":
        encrypt(original_text=text,shift_amount=shift)
    elif direction=="decode":
        decrypt(original_text=text,shift_amount=shift)
    choice=input("do u want to go again?").lower()
    if choice=="no":
     continue1=False
     print("goodbye")
