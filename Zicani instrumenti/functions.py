def pecatiInstrumenti(m1,lista_mandolini):
    for intsrument in lista_mandolini:
        if intsrument.return_strings() == m1.return_strings():
            intsrument.printaj_mandolina()