from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from animais.models import Animal
from pesagens.models import Pesagem
from django.utils.dateparse import parse_date
from decimal import Decimal
from animais.models import HistoricoLoteAnimal

class ImportarPesagensCSV(APIView):
 def post(self, request, lote_id, format=None):
  arquivo = request.FILES.get('file')
  if not arquivo:
   return Response ({"erro": "Nenhum arquivo enviado"}, status = 400)
  
  try:
    conteudo = arquivo.read().decode("utf-8")
    sample = conteudo[:2048]
    dialect = csv.Sniffer().sniff(sample, delimiters=";,")
    delimitador = dialect.delimiter
    dados = conteudo.splitlines()
    leitor = csv.DictReader(dados, delimiter=delimitador)
  except Exception as e:
    return Response(
      {"erro": f"Não foi possível ler o arquivo: {e}"},
      status=status.HTTP_400_BAD_REQUEST
    )

  inseridos = 0
  erros = []

  for linha in leitor:
   try:
    brinco = linha.get("VID")
    classificacao = linha.get("CLASSIFICACA")
    data = parse_date(linha.get("Date"))
    sexo = "F"
    if linha.get("SEXO") == "MACHO":
     sexo = "M"
    peso = linha.get("PESO")
    if not brinco:
     raise Exception("Brinco vazio")

     # converte peso
    peso = peso.replace(",", ".")
    peso = Decimal(peso)

    animal, criado = Animal.objects.get_or_create(
     brinco = brinco,
     defaults = {
      "sexo": sexo,
      "lote_id": lote_id
     }
    )

    lote_atual = animal.lote_id

    if lote_atual != lote_id:
      # registra histórico
      HistoricoLoteAnimal.objects.create(
        animal=animal,
        lote_origem_id=lote_atual,
        lote_destino_id=lote_id,
        data=data,
        origem="importacao"
      )

    # atualiza animal
    animal.lote_id = lote_id
    animal.status = "transferido"
    animal.save()
    pesagem, created = Pesagem.objects.update_or_create(
      animal=animal,
      data=data,
      classificacao=str(classificacao),
      defaults={
        "peso": peso,
        "origem": "importacao"
      }
    )
    pesagem_anterior = (
      Pesagem.objects
      .filter(animal=animal, data__lt=data)
      .order_by("-data")
      .first()
    )

    if pesagem_anterior:
      dias = (data - pesagem_anterior.data).days
      if dias > 0:
        gmd = (peso - pesagem_anterior.peso) / Decimal(dias)
        pesagem.gmd_calculado_automatico = gmd.quantize(Decimal("0.000")) 
        pesagem.save()

    inseridos += 1
   except Exception as e:
    erros.append(f"Erro na linha '{linha}': {e}")
    continue

  return Response({
   "mensagem": f"Importação concluída",
   "pesagens_inseridas": inseridos,
   "erros": erros 
  })


