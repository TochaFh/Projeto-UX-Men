from carta_magic import CartaMagic, TipoCarta

# resolve os danos de uma batalha 1xMANY considerando mecânicas de iniciativa e golpe duplo
def batalha_criaturas(atacante: CartaMagic, bloqueadores: list[CartaMagic]) -> str:
    if atacante.tipo != TipoCarta.CRIATURA or any(b.tipo != TipoCarta.CRIATURA for b in bloqueadores):
        raise ValueError("Todas as cartas devem ser do tipo Criatura para a batalha.")
    
    bloqueadores_inicio = bloqueadores.copy()

    # DANO DE INICIATIVA
    for bloqueador in bloqueadores:
        inflingir_danos(atacante, bloqueador, iniciativa=True)

    # exclui bloqueadores que morreram
    bloqueadores = [b for b in bloqueadores if not b.morreu()]

    if len(bloqueadores) > 0 and not atacante.morreu():

        # DANO BASICO

        # refresh poder de ataque (que foi subtraindo conforme batia)
        atacante.resetar_poder()
        for b in bloqueadores:
            b.resetar_poder()

        for bloqueador in bloqueadores:
            inflingir_danos(atacante, bloqueador)

    # refresh poder de ataque (que foi subtraindo conforme batia)
    atacante.resetar_poder()
    for b in bloqueadores_inicio:
        b.resetar_poder()

    resumo = f"***** BATALHA *****\n"
    resumo += str(atacante)
    resumo += '\n'.join([str(b) for b in bloqueadores_inicio])
    resumo += "*******************\n"
    return resumo
    

# faz o "cruzamento" de dano (básico ou iniciativa)
def inflingir_danos(criatura1: CartaMagic, criatura2: CartaMagic, iniciativa: bool = False) -> str:
    if iniciativa:
        # 2 bate em 1
        criatura1.tomar_dano(criatura2.dano_de_iniciativa())
        criatura2.ataque(criatura1.resistencia)

        # 1 bate em 2
        criatura2.tomar_dano(criatura1.dano_de_iniciativa())
        criatura1.ataque(criatura2.resistencia)
    else:
        # 2 bate em 1
        criatura1.tomar_dano(criatura2.dano_basico())
        criatura2.ataque(criatura1.resistencia)

        # 1 bate em 2
        criatura2.tomar_dano(criatura1.dano_basico())
        criatura1.ataque(criatura2.resistencia)