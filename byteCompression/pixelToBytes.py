import math

def pixel_normallize(pix, width,heigh):
    res_x=pix[0]/width
    res_y=pix[1]/heigh
    return [res_x,res_y]


#pixel is adecimal number smaller than 1
def pixel_to_int(pix):
    pix[0]= pix[0]* math.pow(2,16)
    pix[1] = pix[1] * math.pow(2,16)
    pix[0]= int(pix[0])
    pix[1] = int(pix[1])
    return pix


def int_to_pixel(i_x):
    i_x[0] = i_x[0]/(math.pow(2,16))
    i_x[1]=  i_x[1]/(math.pow(2,16))
    return i_x


def int_to_bytes_touple(x):
    return [int_to_bytes(x[0]),int_to_bytes(x[1])]

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes_touple(x):
    return [int_from_bytes(x[0]),int_from_bytes(x[1])]

def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


test=pixel_normallize((200,300), 2000,1000)
print(test)
test_float=pixel_to_int(test)
print(test_float)


#test_bytes=[int_to_bytes(test_float[0]),int_to_bytes(test_float[1])]
test_bytes=int_to_bytes_touple(test_float)
print(len(test_bytes))

#test_int=[int_from_bytes(test_bytes[0]),int_from_bytes(test_bytes[0])]
test_int=int_from_bytes_touple(test_bytes)
print(test_int)

test_pixel =int_to_pixel(test_int)

print(test_pixel)