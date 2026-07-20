'''
Arquivos do tipo
txt -> arquivo em bloco de notas, texto simples;
csv -> arquivo em excel e google planilhas, texto simple, separado por vírgula;
json -> arquvo em formato de dicionário, texto simples, separado por vírgula;
'''



arquivo_read = open('arquivo_leitura.txt', 'r')

conteudo_arquivo = arquivo_read.readlines()

print(conteudo_arquivo[4], end='')
print(conteudo_arquivo[6], end='')

arquivo_read.close()