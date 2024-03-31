<!DOCTYPE html>
<html>
  <body>
    <img align="right" alt="Coding" width="350" src="https://user-images.githubusercontent.com/113009998/233772381-b051a566-85af-4f28-a6e1-5aa209f37318.png">
    <h1>Assignment for the position tech. support</h1>
    <p>Данное задание направлено на создание скрипта на Python для сбора данных с веб-сайта <a href="https://www.moex.com/">Московская биржа</a></p>
    <p>OC - Windows 11 (Если вы используете Linux, то у вас будет python3 и pip3)</p>
    <p>ПО - Python 3.10</p>
    <p>Stack:</p>    
    <ul>
        <li>requests - Сбор информации</li>
        <li>pandas -  Обработка информации</li>
        <li>openpyxl - Работа с таблицами</li>
        <li>smtp - Отправка сообщений</li>
    </ul>
    <h2>Содержание</h2>
    <ul>
      <li><a href="#install_p">Установка проекта</a></li>
      <li><a href="#install_v">Установка виртуального окружения</a></li>
      <li><a href="#install_r">Установка дополнительных библиотек</a></li>
      <li><a href="#env">Заполнение .env</a></li>
      <li><a href="#run"> Запуск скрипта</a></li>
    </ul>
    <h1 id="install_p">Установка проекта</h1>
    <pre><code>git clone https://github.com/Peskovatskow-Ignat/EvoSoft </code></pre> <p>Так же можно просто скачать zip архив</p>
    <h1 id="install_v">Установка виртуального окружения</h1>
    <pre><code>python -m venv venv</code></pre>
    <p>Активирование venv:</p>
    <p>Windows:</p>
    <pre><code>.\venv\Scripts\activate</code></pre>
    <p>Linux:</p>
    <pre><code>source venv/bin/activate</code></pre>
    <h1 id="install_r">Установка дополнительных библиотек</h1>
    <pre><code>pip install -r requirements.txt</code></pre>
    <h1 id=".env">Содержимое файла .env</h1>
    <pre><code>
SMTP_USERNAME='example@gmail.com'
EMAIL_PASSWORD='xxx xxx xxx xxx'
RECIPIENT_EMAIL='example@yandex.ru'

    </code></pre>
    <h1 id="install_r">Запуск скрипта</h1>
    <pre><code>python main.py</code></pre>
  </body>
</html>
