from carta_magic import CartaMagic, TipoCarta

def batalha_criaturas(criatura1: CartaMagic, criatura2: CartaMagic) -> str:
    if criatura1.tipo != TipoCarta.CRIATURA or criatura2.tipo != TipoCarta.CRIATURA:
        raise ValueError("Ambas as cartas devem ser do tipo Criatura para a batalha.")

    criatura1.resistencia -= criatura2.poder
    criatura2.resistencia -= criatura1.poder

    resultado = f"***** BATALHA *****\n"
    resultado += str(criatura1)
    resultado += str(criatura2)
    resultado += "*******************\n"
    return resultado
    