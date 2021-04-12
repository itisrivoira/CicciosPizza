<?php

    session_start();

    $flag = 0;

    // Nome
    if (empty($_POST["name"])) {
        echo "Name is required ";
    } else {
        if ($_SESSION['name'] == $_POST["name"]){
            // va bene
        } else {
            $flag = 1;
        }
    }

    // Password
    if (empty($_POST["password"])) {
        echo "Password is required ";
    } else {
        if ($_SESSION['password'] == $_POST["password"]){
            // va bene
        } else {
            $flag = 1;
        }
    }

    if($flag == 0){
        echo "Collegato correttamente";
        header("refresh:1; url=index.php");
    }
    if($flag == 1){
        echo "Nome utente o password errati";
        header("refresh:2; url=login.php");
    }
?>