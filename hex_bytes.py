import pickle as pk

def to_hex(obj):
    b = pk.dumps(obj)
    return b.hex()

def from_hex(h):
    b = bytes(bytearray.fromhex(h))
    return pk.loads(b)

if __name__ == '__main__':
    data = {'a': 123}
    print(f'Original Data: {data}')
    h = to_hex(data)
    print(f'Hex of the Data: {h}')
    print(f'Class of Hex: {type(h)}')
    data2 = from_hex(h)
    print(f'Recover Data from Hex: {data2}')
    print(f'data == data2: {data == data2}')
