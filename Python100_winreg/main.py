# work on in windows
# -*- coding=utf-8 -*-
import winreg

def retrieve_reg(key = r'Test\\'):
    try:
        print("retrieve_reg().")
        keyOpen = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, key)
        value = winreg.QueryValueEx(keyOpen,'TestKey')
        print(f'value is:{value}')
        winreg.CloseKey(keyOpen)
        return True
    except Exception as e:
        print(e)
    return False

retrieve_reg()