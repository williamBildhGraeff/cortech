from rest_framework.response import Response
class ImportExportValidator:
    @staticmethod  
    def validar_exportar_pesagem(lote_id):
       if not lote_id:
            return Response({"erro": "Informe ?lote_id=id"}, status=400)