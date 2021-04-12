<?php
    session_start();

    $flag = 0;

    // Nome
    if (empty($_POST["name"])) {
        echo "Name is required ";
    } else {
        $_SESSION['name'] = $_POST["name"];
    }

    // Cognome
    if (empty($_POST["surname"])) {
        echo "Surname is required ";
    } else {
        $_SESSION['surname'] = $_POST["surname"];
    }

    // Mail
    if (empty($_POST["mail"])) {
        echo "Mail is required ";
    } else {
        // controlli
        if ( strstr( $_POST["mail"], '.') and strstr( $_POST["mail"], '@')) {
            $_SESSION['mail'] = $_POST["mail"];
        } else {
            $flag = 1;
        }
    }

    // Username
    if (empty($_POST["username"])) {
        echo "Username is required ";
    } else {
        // controlli
        if(strlen($_POST["username"]) == 0){
            $flag = 1;
        } else {
            $_SESSION['username'] = $_POST["username"];
        }
    }

    // Password
    if (empty($_POST["password"])) {
        echo "Password is required ";
    } else {
        // controlli
        if(strlen($_POST["password"]) < 8){
            $flag = 1;
        } else {
            $_SESSION['password'] = $_POST["password"];
        }
    }

    // Confpassword
    if (empty($_POST["confpassword"])) {
        echo "ConfPassword is required ";
    } else {
        if($_POST["confpassword"] != $_POST["password"]){
            $flag = 1;
        }
    }

    if($flag == 1){
        echo "Dati immessi in modo errato";
        header("refresh:2; url=signin.php");
    } else {
        header("Location: ./login.php");
    }

    
?>