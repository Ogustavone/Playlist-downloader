from pytube import Playlist, YouTube
import os

def criar_lista_txt(link_playlist):
    try:
        # Obtém a playlist a partir do link e extrai os links dos videos
        playlist = Playlist(link_playlist)
        links_videos = [video_url for video_url in playlist.video_urls]
        
        # Salva os links em um arquivo de texto
        with open('lista_playlist.txt', 'w') as arquivo:
            arquivo.write('\n'.join(links_videos))
        
        print(f'Lista de reprodução salva com sucesso em lista_playlist.txt.')
        
        # Chama a função que começa a baixar os vídeos
        baixar_videos()
    except Exception as e:
        print(f'Erro ao processar a playlist: {str(e)}')
        parar()

def baixar_videos():
     # Abre o arquivo de texto como leitura
    with open('lista_playlist.txt', 'r') as file:
        links = file.read().splitlines()

    for i, link in enumerate(links, start=1):

        try:
            # Obtém informações do vídeo a partir do link
            video = YouTube(link)
            titulo_video = video.title

            # Filtra o download para "apenas audio", na melhor qualidade disponível
            stream = video.streams.filter(only_audio=True).first()

             # Define o nome do arquivo final com a extensão mp3
            nome_arquivo = f'{titulo_video}.mp3'

            # Faz o download para a pasta download_mp3
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

def validar_link_youtube(link):
    dominios_validos = ["youtube.com", "m.youtube.com", "youtu.be"]
    
    for dominio in dominios_validos:
        if dominio in link:
            return True
    
    return False

def parar():
    # Verifica que a lista ainda está na pasta para excluí-la
    if os.path.exists("lista_playlist.txt"):
        try:
            os.remove("lista_playlist.txt")
            
        except Exception as e:
            print(f'Erro ao remover o arquivo: {str(e)}')

        # Entrada do usuário para reiniciar ou parar o programa
    resposta = input("Deseja continuar (s/n)? ")
    if resposta.upper() == "S" or resposta.upper() == "SIM":
        main_app()
    else:
        quit()

# Pasta de destino para os vídeos baixados
pasta_destino = 'downloads_mp3'

# Certifica de que a pasta de destino existe, se não, ela é criada novamente
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

def main_app():

    print("---" * 16)
    print("Mp3 Playlist downloader - Feito por Gustavo")
    print("Visite meu perfil: https://github.com/Ogustavone")
    print("---" * 16)

    # Entrada do usuário - URL playlist
    link_playlist = input("Digite o link da playlist do YouTube: ")

    # Se não passar pela validação do link, o programa para
    if not validar_link_youtube(link_playlist):
        print("O link inserido não parece ser um link válido do YouTube.")
        parar()
        

    # Aguardar interação do usuário para começar
    input("Pressione Enter para continuar... ")

    # Chama a função que faz uma lista de todos os links em txt
    criar_lista_txt(link_playlist)

# Faz a função principal rodar
main_app()