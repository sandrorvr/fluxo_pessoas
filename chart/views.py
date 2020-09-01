from django.shortcuts import render
from .models import fluxo
import json
from datetime import datetime

def maxMin(time,total,inter,flag):
    aux = []
    intervalo = inter
    auxSup = intervalo
    auxInf = 0
    laco = len(total)//intervalo

    for _ in range(laco):
        aux.append(sum(total[auxInf:auxSup]))
        auxSup += intervalo
        auxInf += intervalo

    if flag == 'max':
        indMaior = aux.index(max(aux))
        print(indMaior)

    elif flag == 'min':
        indMaior = aux.index(min(aux))

    else:
        indMaior = aux.index(max(aux))

    indInf = abs(indMaior*intervalo-intervalo)+6
    indSup = indInf+intervalo
    #print(aux, indInf,indSup)
    return (time[indInf],time[indSup])


def index(request):
    dia = datetime.now().date().isoformat()
    if request.method == 'POST':
        dia = request.POST['dataBusca']
    data = fluxo.objects.all()
    time = []
    total = []
    for linha in data:
        if linha.date_pes.isoformat() == dia:
            time.append(linha.time_pes.strftime('%H:%M'))
            total.append(linha.total_pes)

    MenorInt, MaiorInt = maxMin(time,total,6,'max')
    menorInt, maiorInt = maxMin(time,total,6,'min')
    t_pes = sum(total)
    time = json.dumps(time)
    total = json.dumps(total)

    context = {
        'time': time,
        'total':total,
        'dia':dia,
        't_pes': t_pes,
        'MaiorInt':MaiorInt,
        'MenorInt':MenorInt,
        'maiorInt':maiorInt,
        'menorInt':menorInt
    }
    return render(request, 'index.html', context)
