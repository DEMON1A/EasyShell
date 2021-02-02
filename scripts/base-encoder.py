import base64

def Run(Input):
    BInput = Input.encode('UTF-8')
    Encoded = base64.b64encode(BInput)

    Encoded = Encoded.decode('UTF-8')
    print("Base64:" , Encoded)
