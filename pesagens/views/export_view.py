from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from animais.models import Animal
from pesagens.models import Pesagem
import csv

class ExportarCsvPesagem(APIView):
    def get(self, request):
        lote_id = request.GET.get("lote_id")
        if not lote_id:
            return Response({"erro": "Informe ?lote_id=id"}, status=400)

        animais = Animal.objects.filter(lote_id=lote_id)

        response = HttpResponse(
            content_type='text/csv; charset=utf-8'
        )
        response['Content-Disposition'] = (
            f'attachment; filename="pesagens_lote_{lote_id}.csv"'
        )

        writer = csv.writer(response, delimiter=';')

        # ============================
        # 1. Calcular max_pesagens
        # ============================
        max_pesagens = 0
        for animal in animais:
            qtd = Pesagem.objects.filter(animal=animal).count()
            if qtd > max_pesagens:
                max_pesagens = qtd

        # ============================
        # 2. HEADER (ESCREVE UMA VEZ)
        # ============================
        header = ['Brinco']
        for i in range(1, max_pesagens + 1):
            header += [f'data_{i}', f'peso_{i}', f'gmd_{i}']
        header.append("gmd_medio")

        writer.writerow(header)

        # ============================
        # 3. Linhas dos animais
        # ============================
        for animal in animais:
            linha = [animal.brinco]

            pesagens = Pesagem.objects.filter(animal=animal).order_by('data')
            gmds = []

            for p in pesagens:
                linha.append(str(p.data))
                linha.append(str(p.peso))
                linha.append(str(p.gmd_calculado_automatico) if p.gmd_calculado_automatico else "")

                if p.gmd_calculado_automatico:
                    gmds.append(float(p.gmd_calculado_automatico))

            # Preencher vazios
            faltam = max_pesagens - pesagens.count()
            linha += ['-', '-', '-'] * faltam

            # GMD médio
            gmd_medio = sum(gmds) / len(gmds) if gmds else ""
            linha.append(gmd_medio)

            writer.writerow(linha)

        return response
