<?php
    $errorMSG = "";

    // NAME
    if (empty($_POST["name"])) {
        $errorMSG = "Name is required ";
    } else {
        $name = $_POST["name"];
    }

    // EMAIL
    if (empty($_POST["email"])) {
        $errorMSG .= "Email is required ";
    } else {
        $email = $_POST["email"];
    }

    // MESSAGE
    if (empty($_POST["message"])) {
        $errorMSG .= "Message is required ";
    } else {
        $message = $_POST["message"];
    }

    if($_POST["Message"]) {
        $EmailTo = "alessandro.lopez320@gmail.com";
        $Subject = "Messaggio dal sito";

        $Body = "";
        $Body .= "Name: ";
        $Body .= $name;
        $Body .= "\n";
        $Body .= "Email: ";
        $Body .= $email;
        $Body .= "\n";
        $Body .= "Message: ";
        $Body .= $message;
        $Body .= "\n";

        // invia l'email
        mail($EmailTo, $Subject, $Body, "From:".$email);
    }
?>