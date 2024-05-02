from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        restaurant = request.form['restaurant']
        character = request.form['character']

        # Imprimir os dados na tela
        print(f'Nome: {name}')
        print(f'Email: {email}')
        print(f'Restaurante: {restaurant}')
        print(f'Sobre o Jantar: {character}')

        # Configurar o email
        msg = MIMEText(f'Nome: {name}\nEmail: {email}\nRestaurante: {restaurant}\nSobre o Jantar: {character}')
        msg['Subject'] = 'Pedido Pindolinha, chegou!'
        msg['From'] = 'fatimabeatriz.nasc@gmail.com'  # Substitua pelo seu email
        msg['To'] = 'fatimabeatriz.nasc@gmail.com'  # Substitua pelo email do destinatário

        # Enviar o email e retornar a mensagem para exibição na tela
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login('fatimabeatriz.nasc@gmail.com', 'gxss npzz esjq zvyc')  # Substitua pelo seu email e senha
            smtp.send_message(msg)
            smtp.quit()
            return 'Email enviado com sucesso!<br>' + str(msg)
        except Exception as e:
            return f'Erro ao enviar o email: {e}'

if __name__ == '__main__':
    app.run(debug=True)
