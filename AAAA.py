import base64

input_string = "U3Vubnk="
base64_converted_string = input_string.encode("ascii")
decode = base64.b64decode(base64_converted_string)
decimal_converted_string = decode.decode("ascii")

print(decimal_converted_string)