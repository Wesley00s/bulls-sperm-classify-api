def calc_classify(data):
    points = 0

    data = dict(data)

    zptz_totais = data["zptz_106"] * data["volume"]
    def_men_percent = 100 - (data["def_mai_percent"] + data["normais_percent"])
    def_men = 200 - (data["normais"] + data["def_mai"])

    data.update({"zptz_totais": zptz_totais})
    data.update({"def_men_percent": def_men_percent})
    data.update({"def_men": def_men})

    mot_massal = data['turbilhao']
    mot_percent = data['mot_moveis']
    def_mai = data['def_mai_percent']
    def_total = def_mai + data['def_men_percent']
    idade_meses = data['idade']
    circunferencia = data['ce']

    # Motilidade espermática
    if mot_massal == 5 and mot_percent > 70:
        points += 20
    elif 4 < mot_massal < 5 and 60.0 < mot_percent <= 70.0:
        points += 12
    elif mot_massal == 4 and 50.0 < mot_percent <= 60.0:
        points += 10
    elif 0 < mot_massal <= 3 and mot_percent < 50.0:
        points += 3

    # Morfologia espermática
    if def_mai <= 10.0 and def_total <= 25.0:
        points += 40
    elif 10.0 < def_mai <= 19.0 and 26.0 < def_total <= 39.0:
        points += 25
    elif 20.0 < def_mai <= 29.0 and 40.0 < def_total <= 59.0:
        points += 10
    elif def_mai > 29.0 and def_total > 59.0:
        points += 3

    # Circunferência escrotal
    if 18 < idade_meses <= 23:
        if circunferencia > 30:
            points += 40
        elif 26 < circunferencia < 30:
            points += 24
        else:
            points += 10

    elif 24 < idade_meses <= 29:
        if circunferencia > 34:
            points += 40
        elif 30 < circunferencia < 34:
            points += 24
        else:
            points += 10

    elif 30 < idade_meses <= 41:
        if circunferencia > 36:
            points += 40
        elif 31 < circunferencia < 36:
            points += 24
        else:
            points = points + 10

    elif 42 < idade_meses <= 60:
        if circunferencia > 38:
            points += 40
        elif 32 < circunferencia < 38:
            points += 24
        else:
            points += 10

    elif idade_meses > 60:
        if circunferencia > 39:
            points += 40
        elif 34 < circunferencia < 39:
            points += 24
        else:
            points += 10

    if points > 60:
        data['alvo'] = 0  # Selecionado para reprodução
    elif 60 > points > 40:
        data['alvo'] = 1  # Utilizável para reprodução com restrições
    else:
        data['alvo'] = 2  # Não ápto a reprodução

    return data
