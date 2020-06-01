"""Saber si una palabra es palindromo"""
def main():
    entrada = input("Introduce una palabra: ")

    if entrada == entrada[::-1]:
        print(f"La palabra es palindromo")

    else:
        print(f"No es palindromo")

if __name__ == "__main__":
    main()
