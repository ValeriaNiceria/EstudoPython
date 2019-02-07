"""
Criando uma função para download na web 
"""

# Importando os módulos
import io
# import sys
import urllib.request as request

BUFF_SIZE = 1024

# Download de arquivo de tamanho conhecido
def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for times in range(times):
        output.write(response.read(BUFF_SIZE))
        print('Download %d' % (((times * BUFF_SIZE) / length) * 100))


# Função para download na web
def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))
        
        


# Definindo função main
def main():
    url = 'http://livropython.com.br/dados.zip'
    response = request.urlopen(url)
    out_file = io.FileIO('saida.zip', mode='w')
    
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
        
    response.close()
    out_file.close()
    print('Finished')

if __name__ == "__main__":
    main()
    