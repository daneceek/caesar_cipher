import unicodedata

from sys import stdin, path, stdout
import click


@click.command()
@click.option("--method", "-m", help = "Vyberte metodu | encode nebo decode", type = str, required=True)
@click.option("--files", "-f",  nargs = 2, required=True, help = "Zadejte cestu k souboru, který chcete dekódovat nebo enkódovat a jako druhý argument cestu k výstupu | pomlčka spustí stdin")

def main(method, files):
    
    input, output = files
    if method == "encode":
        folder_opening(input, output, 3)
        
    elif method == "decode":
        folder_opening(input, output, -3)
    else:
        raise Exception("Nebyla zadána platná metoda. Existuje pouze 'encode' a 'decode'")
    print("Šifra dekóduje/enkóduje o tři písmena. Výsledný soubor byl vytvořen/výstup byl vypsán")
def folder_opening(input, output, shift):
    if input == "-" and output == "-":
        print("zadejte text k (de)šifrování:")
        text = caesar(stdin.read(), shift)
        print()
        stdout.write(text)
    elif input == "-":
        print("zadejte text k (de)šifrování:")
        text = caesar(stdin.read(), shift)
        print()
        with open(output, "w") as output:
                output.write(text)
    elif output == "-":
        with open(input, "r") as input:
            text = caesar(input.read(), shift)
            stdout.write(text)
    else:
        with open(input, "r") as input:
            text = caesar(input.read(), shift)
            
            with open(output, "w") as output:
                output.write(text)
    print()
# alphabet = string.ascii_uppercase

def caesar(text:str, key:int):
    text = text.upper()
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").upper() # odstranění znaků s háčkem atd. 
    result = ""
    for char in text:
        if char == "\n":
            result += "\n"
        if char == " ":
            result += " "
        if char >= "A" and char <= "Z":
            position = ord(char) - 65 
            new_position = (position + key) % 26
            result += chr(new_position + 65) 
        else:
            continue    
    return result


if __name__ == "__main__":
    main()