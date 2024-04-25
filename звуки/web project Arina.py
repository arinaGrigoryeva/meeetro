from flask import Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/astronaut_selection')
def bootstrap():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                                 <style type="text/css">
                                   form.login_form {
                                    max-width: 450px;
                                    margin-left: auto;
                                    margin-right: auto;
                                    background-color: #FFA07A;
                                    border: 1px solid gray;
                                    border-radius: 5px;
                                    padding: 10px;
                                   }
                                  </style> 
                              </head>
                                      <body>
                                        <h3 style="position: relative;text-align: center;">Анкета претендента</h3>
                                        <h5 style="position: relative;text-align: center;">На участие в миссии</h5>
                                        <div>
                                            <form class="login_form" method="post">
                                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите имя" name="email">
                                                <input type="password" class="form-control" id="password" placeholder="Введите фамилию" name="password">
                                                <input type="mail" class="form-control" id="mail" aria-describedby="mailHelp" placeholder="Введите адрес почты" name="mail">
                                                <div class="form-group">
                                                    <label for="classSelect">Какое у вас образование? </label>
                                                    <select class="form-control" id="classSelect" name="class">
                                                      <option>Дошкольное</option>
                                                      <option>Начальное общее</option>
                                                      <option>Основное общее</option>
                                                      <option>среднее профессиональное</option>
                                                      <option>Высшее</option>
                                                    </select>
                                                 </div>
                                                 <div class="form-group">
                                                    <label for="form-check">Какие у Вас есть проффесии?</label>
                                                    <div class="form-check">
                                                      <input class="form-check-input" type="radio" name="z" id="male" value="male" checked>
                                                      <label class="form-check-label" for="male">
                                                        инженер-исследователь
                                                      </label>
                                                    </div>
                                                    <div class="form-check">
                                                      <input class="form-check-input" type="radio" name="z" id="female" value="female">
                                                      <label class="form-check-label" for="female">
                                                        пилот
                                                      </label>
                                                    </div>
                                                    <div class="form-check">
                                                      <input class="form-check-input" type="radio" name="z" id="female1" value="female1">
                                                      <label class="form-check-label" for="female1">
                                                        строитель
                                                      </label>
                                                    </div>
                                                    <div class="form-check">
                                                      <input class="form-check-input" type="radio" name="z" id="female2" value="female2">
                                                      <label class="form-check-label" for="female2">
                                                        штурман
                                                      </label>
                                                    </div>
                                                    <div class="form-check">
                                                      <input class="form-check-input" type="radio" name="z" id="female" value="female">
                                                      <label class="form-check-label" for="female">
                                                        гляциолог
                                                      </label>
                                                    </div>
                                                    <div class="form-check">
                                                      <input class="form-check-input" type="radio" name="z" id="female" value="female">
                                                      <label class="form-check-label" for="female">
                                                        метеоролог
                                                      </label>
                                                    </div>
                                                <div class="form-group">
                                                    <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                                </div>
                                                <div class="form-group">
                                                    <label for="photo">Приложите фотографию</label>
                                                    <input type="file" class="form-control-file" id="photo" name="file">
                                                </div>
                                                </div>
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                                </div>
                                                <button type="submit" class="btn btn-primary">Отправить</button>
                                            </form>
                                        </div>
                                      </body>
                                    </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['mail'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['z'])
        return "Анкета претендента"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




