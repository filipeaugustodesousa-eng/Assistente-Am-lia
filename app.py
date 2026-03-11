import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Inicializar o motor de voz (offiline)
engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()
    # faz o computador falar o texto fornecido
    
reconhecedor = sr.Recognizer()
def ouvir():
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = reconhecedor.listen(source)
        try:
            comando = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            return comando
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return ""
        except sr.RequestError:
            print("Erro ao conectar ao serviço de reconhecimento de voz.")
            return ""
        
    # loop principal de execução 
if __name__ == "__main__":
    # Esta linha deve ter 4 espaços de recuo
    falar("Olá, eu sou a Amélia, sua assistente virtual. Em que posso ajudar?")
    
    while True:
        # Tudo aqui dentro deve ter +4 espaços de recuo (total 8)
        comando = ouvir().lower()
        
        if "horas" in comando:
            agora = datetime.datetime.now()
            horas = agora.strftime("%H:%M")
            falar(f"Agora são {horas}")
            
        elif "pesquisar" in comando:
            falar("O que você gostaria de pesquisar?")
            termo = ouvir().lower()
            if termo:
                url = f"https://www.google.com/search?q={termo}"
                webbrowser.open(url)
                falar(f"Pesquisando por {termo} no Google.")
                
        elif "sair" in comando:
            falar("Até mais!")
            break  # Importante para fechar o programa
            
        elif comando == "": # Se ele não ouvir nada, não fala "não entendi" toda hora
            continue
            
        else:
            falar("Desculpe, não entendi o comando.")