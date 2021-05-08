import  telnetlib
def count_phones(phone_load_params: str):
    ip = '10.128.0.177'
    port = '3375'
    with telnetlib.Telnet(ip, port) as t:
        phone = str.encode(phone_load_params)
        csca = phone + b'\n'
        asd = t.write(phone + b'\n')
        print(csca)
        try:
            message = t.read_until(b'\n') # Will not timeout until you have response
            print(message)
            print(message.decode().strip())
            return message.decode().strip()

        except EOFError:            # If connection was closed
            print('connection closed')
            return False

phone = '90638974416'
include_days = '365'
exclude_days = '7'
phone_load_params = phone + ' ' + include_days + ' ' + exclude_days
v = count_phones(phone_load_params)