import base64

def write_data(file_name: str, data: bytes, mode='wb'):
    #bytes to base64
    data = base64.b64encode(data)
    
    with open(file_name, mode='wb') as f:
        f.write(data)
        
def read_data(file_name: str) -> bytes:
    with open(file_name, "rb") as f:
        data = f.read()
    #base64 to bytes
    return base64.b64decode(data)