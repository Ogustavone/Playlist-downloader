from pytube import Playlist, YouTube
import os

def criar_lista_txt(link_playlist):
    try:
        playlist = Playlist(link_playlist)
        links_videos = [video_url for video_url in playlist.video_urls]

        with open('lista_playlist.txt', 'w') as arquivo:
            arquivo.write('\n'.join(links_videos))

        print(f'Lista de reprodução salva com sucesso em lista_playlist.txt.')
        baixar_videos()
    except Exception as e:
        print(f'Erro ao processar a playlist: {str(e)}')
        parar()

def baixar_videos():
    with open('lista_playlist.txt', 'r') as file:
        links = file.read().splitlines()

    for i, link in enumerate(links, start=1):
        try:
            video = YouTube(link)
            titulo_video = video.title
            stream = video.streams.filter(only_audio=True).first()
            nome_arquivo = f'{titulo_video}.mp3'
            stream.download(output_path=pasta_destino, filename=nome_arquivo)
            print(f'Vídeo "{titulo_video}" baixado com sucesso.')
        except Exception as e:
            print(f'Erro ao baixar o vídeo {i}: {str(e)}')
            parar()

    converter_arquivos()

def converter_arquivos():
    if os.path.exists(pasta_destino):
        arquivos_na_pasta = os.listdir(pasta_destino)

        for arquivo in arquivos_na_pasta:
            caminho_arquivo_antigo = os.path.join(pasta_destino, arquivo)
            caminho_arquivo_novo = os.path.join(pasta_destino, f'{os.path.splitext(arquivo)[0]}.mp3')

            if not arquivo.endswith('.mp3') and os.path.isfile(caminho_arquivo_antigo):
                os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)
                print(f'Adicionada a extensão .mp3 para: {caminho_arquivo_novo}')

        print('Concluído.')
        parar()
    else:
        print(f'A pasta {pasta_destino} não foi encontrada.')
        parar()

def parar():
    os.remove("lista_playlist.txt")
    resposta = input("Deseja continuar? ")
    if resposta.upper() == "Y":
        criar_lista_txt(link_playlist)
    else:
        quit()

# Pasta de destino para os vídeos baixados
pasta_destino = 'downloads'

# Certifique-se de que a pasta de destino existe, se não, crie-a
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

link_playlist = input("Digite o link da playlist do YouTube: ")
input("Pressione qualquer tecla para iniciar o programa... ")

criar_lista_txt(link_playlist)
