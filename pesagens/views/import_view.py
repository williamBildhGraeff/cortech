from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from animais.models import Animal
from pesagens.models import Pesagem
from django.utils.dateparse import parse_date

class ImportarPesagensCSV(APIView):
 def post(self, request, format=None):
  arquivo = request.FILES.get('file')
  if not arquivo:
   return Response ({"erro": "Nenhum arquivo enviado"}, status = 400)
  
  try:
   dados = arquivo.read().decode("utf-8").splitlines()
   leitor = csv.DictReader(dados, delimiter = ";")
  except Exception as e:
   return Response ({"erro": "Não foi possível ler o arquivo: {e}"}, status = 400)

  inseridos = 0
  erros = []

  for linha in leitor:
   try:

    brinco = linha.get("VID")
    data = parse_date(linha.get("Date"))
    sexo = "F"
    if linha.get("SEXO") == "MACHO":
     sexo = "M"
    peso = linha.get("PESO")
    if not brinco:
     raise Exception("Brinco vazio")

     # converte peso
    peso = peso.replace(",", ".")
    peso = float(peso)

    animal, criado = Animal.objects.get_or_create(
     brinco = brinco,
     defaults = {
      "sexo": sexo,
      "lote_id": 1
     }
    )

    Pesagem.objects.create(
     animal = animal,
     peso = peso,
     data = data,
     origem = "importacao"
    )

    inseridos += 1
   except Exception as e:
    erros.append(f"Erro na linha '{linha}': {e}")
    continue

  return Response({
   "mensagem": f"Importação concluída",
   "pesagens_inseridas": inseridos,
   "erros": erros 
  })


