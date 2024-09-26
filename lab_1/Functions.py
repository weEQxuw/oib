import json 
from pathlib import Path


def ReadTheKey(FilePath: str) -> dict[str, str]:
    """Reads the file with the decryption key"""
    try:
        FilePath = Path(FilePath)
        with open(FilePath, "r", encoding = "utf-8") as File:
            Data = json.load(File)
            return Data
    except:
        return None


def ReadTheText(FilePath: str) -> str:
    """Reads the text from the file"""
    try:
        FilePath = Path(FilePath)
        with open(FilePath, "r", encoding = "utf-8") as File:
            Src = File.read()
            return Src
    except:
        return None


def Decryption(Text: str, Key: dict[str, str]) -> str:
    """Decrypts text by key"""
    Src = ""
    if Text == None or Key == None:
        return "Отсутствует текст либо ключ шифрования!"
    try:
        for Symbol in Text:
            if Symbol in Key.keys():
                Src += Key[Symbol]
            else:
                Src += Symbol
    except:
        return "При попытке расшифровать текст произошла ошибка!"
    return Src


def Encryption(Text: str, Key: dict[str, str]) -> str:
    """Encrypts text by key"""
    Src = ""
    if Text == None or Key == None:
        return "Отсутствует текст либо ключ шифрования!"
    Text = Text.upper()
    Keys = list(Key.keys())
    Values = list(Key.values())
    try: 
        for symbol in Text:
            if symbol in Values:
                Src += Keys[Values.index(symbol)]
            else:
                Src += symbol
    except: 
        return "При попытке зашифровать текст возникла ошибка!"
    return Src


def TheFreqAnalysis(Text: str) -> dict:

    Dic = dict()
    
    for i in Text:
        if i in Dic:
            Dic[i] += 1
        else:
            Dic[i] = 1

    for k in Dic.keys():
        Dic[k] = Dic[k] / len(Text)

    return Dic


def SaveFreqAnalysis(FilePath: str, Text: str) -> None:
    """Saves the character frequency in a json file"""
    FilePath = Path(FilePath)

    with open(FilePath, 'w', encoding = "utf-8") as File:
        json.dump(TheFreqAnalysis(Text), File)