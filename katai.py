
def rgb_to_hex(a,b,c):

    if((a>=0 and a<=255) and (b>=0 and b<=255) and (c>=0 and c<=255)):
        hex_color = '#{:02x}{:02x}{:02x}'.format(a,b,c)

        print( hex_color)

    else:
        raise ValueError(" Error")


#rgb_to_hex(42,45,60)
