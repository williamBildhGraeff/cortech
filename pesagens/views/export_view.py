from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from core.services.export_services import exportar_pesagens_lote_csv
import csv

class ExportarCsvPesagem(APIView):
    def get(self, request):
        lote_id = request.GET.get("lote_id")
        if not lote_id:
            return Response({"erro": "Informe ?lote_id=id"}, status=400)

        resultado = self.exportar_pesagens_lote_csv(lote_id)

        response = HttpResponse(
            content_type='text/csv; charset=utf-8'
        )
        response['Content-Disposition'] = (
            f'attachment; filename="pesagens_lote_{lote_id}.csv"'
        )

        writer = csv.writer(response, delimiter=';')
        header = ['Brinco']    
        for i in range(1, resultado['max_pesagens'] + 1):
            header += [f'data_{i}', f'peso_{i}', f'gmd_{i}']
        header.append("gmd_medio")
        writer.writerow(header)

        for item in resultado['dados']:
            linha = [item['brinco']]
            for pesagem in item['pesagens']:
                linha.append(pesagem['data'])
                linha.append(pesagem['peso'])
                linha.append(pesagem['gmd_calculado_automatico'])
            # Preencher vazios
            faltam = resultado['max_pesagens'] - len(item['pesagens'])
            linha += ['-', '-', '-'] * faltam
            linha.append(item['gmd_medio'])
            writer.writerow(linha)  

        return response
