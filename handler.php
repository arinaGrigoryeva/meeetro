<?php
    if (!empty($_POST)) { //если нажали кнопку отправить
        $fname_u = $_POST['fname']; //создаем переменные для отправки
        $email_u = $_POST['email'];
        $message_u = $_POST['message'];
        $message = "От ".$fname_u." <".$email_u.">\Отзыв:".$message_u."/Дата: ".date("j M Y")."/Время: ".date("h:i")."."; //сообщение будет выглядеть так: От ИМЯ <email@mail.ru>/Отзыв: текст отзыва/Дата: число отправки/Время: время отправки.
        mail('Arina2030620@yandex.ru', 'Отзыв с сайта site.ru', $message); //сама функция отправки почты
        echo "Сообщение успешно отправлено, спасибо";//если сообщение отправлено успешно, то выходит это сообщение
    }
?>