import os
import datetime
import pandas as pd


dict_morse = {"O", "L", "A",  "M", "U", "N", "D", "O"}
msg = ' '
file_path = "decode_morse.csv"

def decode_morse(msg, dict_morse):
    msg_lst = msg.split(" ")
    msg_claro = [] 
    for letter in msg_lst :
        msg_claro.append(dict_morse[letter])
    return "".join(msg_claro)


def save_clear_msg_csv_hdr(file_path, msg, dict_morse):
    now = datetime.datetime.now()
    msg_claro = decode_morse(msg,dict_morse)
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    if not os.path.exists(file_path):
        hdr = True
    else:
        hdr = False
    #hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode='a', index=False, header=hdr)


if __name__ == "__main__":
    save_clear_msg_csv_hdr(file_path, msg, dict_morse)
