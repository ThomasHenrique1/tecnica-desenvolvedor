def inverter_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Informe uma string para inverter: ")
    print("String invertida:", inverter_string(string))