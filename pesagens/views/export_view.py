from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import csv
from pesagens.validators.import_export_validators import ImportExportValidator
from pesagens.services.export_pesagens import ExportarCsvPesagemService
from lote.models import Lote
class ExportarCsvPesagem(APIView):
    """
    Exporta as pesagens de um lote para um arquivo CSV.
    """
    def get(self, request):
        lote_id = request.GET.get("lote_id")
        lote_nome = Lote.objects.get(id=lote_id).nome
        ImportExportValidator.validar_exportar_pesagem(lote_id)

        try:
            resultado = ExportarCsvPesagemService.exportar_pesagens_lote_csv(lote_id)
        except Exception as e:
            return Response({"erro": str(e)}, status=400)

        response = HttpResponse(
            content_type='text/csv; charset=utf-8'
        )
        response['Content-Disposition'] = (
            f'attachment; filename="pesagens_lote_{lote_nome}.csv"'
        )

        writer = csv.writer(response, delimiter=';')
        header = ['Brinco']    
        for i in range(1, resultado['max_pesagens'] + 1):
            header += [f'Data', f'Peso', f'GMD', f'Classificacao']
        header.append("GMD Medio")
        writer.writerow(header)

        for item in resultado['dados']:
            linha = [item['brinco']]
            for pesagem in item['pesagens']:
                linha.append(pesagem['data'])
                linha.append(pesagem['peso'])
                linha.append(pesagem['gmd_calculado_automatico'])
                linha.append(pesagem['classificacao'])
            # Preencher vazios
            faltam = resultado['max_pesagens'] - len(item['pesagens'])
            linha += ['-', '-', '-', '-'] * faltam
            linha.append(item['gmd_medio'])
            writer.writerow(linha)  

        return response
