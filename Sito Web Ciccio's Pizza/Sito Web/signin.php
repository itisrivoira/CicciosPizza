<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">

		<title>Ciccio's Pizza</title>
		
		<link rel="shortcut icon" href="images/chef.png" type="image/x-icon">
		<link rel="apple-touch-icon" href="images/chef.png">

		<link rel="stylesheet" href="css/bootstrap.min.css">    
		<link rel="stylesheet" href="css/style.css">
	</head>

	<body>
		<header class="top-navbar">
			<nav class="navbar navbar-expand-lg navbar-light bg-light">
				<div class="container">
					<a class="navbar-brand" href="index.php">
						<img src="images/logo.png" alt="" width="142" height="117"/>
					</a>
					<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbars-rs-food" aria-controls="navbars-rs-food" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
					</button>
					<div class="collapse navbar-collapse" id="navbars-rs-food">
						<ul class="navbar-nav ml-auto">
							<li class="nav-item"><a class="nav-link" href="index.php">Home</a></li>
							<li class="nav-item"><a class="nav-link" href="aboutus.php">Chi siamo</a></li>
							<li class="nav-item"><a class="nav-link" href="rules.php">Regole</a></li>
							<li class="nav-item"><a class="nav-link" href="contact.php">Contattaci</a></li>
							<li class="nav-item "><a class="nav-link" href="login.php">Login</a></li>
                            <li class="nav-item active"><a class="nav-link" href="signin.php">Registrati</a></li>
							<li class="nav-item"><a class="nav-link" href="gioco.zip">Download</a></li>
						</ul>
					</div>
				</div>
			</nav>
		</header>
		
		<div class="all-page-title page-breadcrumb">
			<div class="container text-center">
				<div class="row">
					<div class="col-lg-12">
						<h1>Registrati</h1>
					</div>
				</div>
			</div>
		</div>
		<br>
		<div class="container">
			<div class="row">
				<div class="col-lg-12">
					<div class="heading-title text-center"><br><br>
						<h2>Pagina di Registrazione</h2>
						<p>Completa il form per registarti</p>
						<br>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="col-lg-12 col-sm-12 col-xs-12">
					<div class="contact-block">
						<form method="POST" id="loginForm" action= "register.php">
                            <div class="row">
								<div class="col-md-12">
									<div class="form-group">
										<input type="text" placeholder="Nome" id="name" class="form-control" name="name" required data-error="Please enter your name">
									</div> 
								</div>
							</div>
                            <div class="row">
								<div class="col-md-12">
									<div class="form-group">
										<input type="text" placeholder="Cognome" id="surname" class="form-control" name="surname" required data-error="Please enter your surname">
									</div> 
								</div>
							</div>
                            <div class="row">
								<div class="col-md-12">
									<div class="form-group">
										<input type="text" placeholder="Mail" id="mail" class="form-control" name="mail" required data-error="Please enter your mail">
									</div> 
								</div>
							</div>
							<div class="row">
								<div class="col-md-12">
                                    <div class="form-group">
                                        <input type="text" placeholder="Nome utente" id="userName" class="form-control" name="username"  required data-error="Please enter your username">
                                    </div>
								</div>
							</div>
							<div class="row">
								<div class="col-md-12">
									<div class="form-group">
										<input type="password" placeholder="Password" id="password" class="form-control" name="password" required data-error="Please enter your password">
									</div> 
								</div>
							</div>
                            <div class="row">
								<div class="col-md-12">
									<div class="form-group">
										<input type="password" placeholder="Conferma password" id="confPassword" class="form-control" name="confpassword" required data-error="Please enter your password">
									</div> 
								</div>
							</div>
							<div class="row">
								<div class="col-md-4"></div>
								<div class="col-md-4">
									<div class="submit-button text-center"> <br>
										<button class="btn btn-common" id="submit" type="submit">Registrati</button>
										<div id="btnRegistrati" class="h3 text-center hidden"></div> 
									</div>
								</div><div class="col-md-4"></div>
							</div>      
						</form>
					</div>
				</div>
			</div>
		</div><br><br>

		<footer class="footer-area bg-f">
			<div class="container">
				<div class="row">
					<div class="col-lg-6 col-md-6">
						<h3>Per contattarci</h3>
						<p><b>Chiabrando Lorenzo</b></p>
						<p>Bonagemma Alberto</p>
						<p>Lopez Alessandro</p>
						<p>Tenca Francesco</p>
						<p>Hila Flavian</p>
						<br>
					</div>
					<div class="col-lg-6 col-md-6">
						<h3><br></h3>
						<p>lorenzo.chiabrando02@gmail.com</p>
						<p>albibonagemma@gmail.com</p>
						<p>lopezmarino.alessandro@denina.com</p>
						<p>frate022@gmail.com</p>
						<p>flavianhila@gmail.com</p>
					</div>
					<div class="col-lg-12 col-md-12">
						<h3>I Nostri social</h3>
						<ul class="list-inline f-social">
							<li class="list-inline-item"><a href="https://facebook.com"><i class="fa fa-facebook"></i></a></li>
							<li class="list-inline-item"><a href="https://instagram.com"><i class="fa fa-instagram"></i></a></li>
							<li class="list-inline-item"><a href="https://twitter.com"><i class="fa fa-twitter"></i></a></li>
							<!-- Devo mettere anche github e  -->
						</ul>
					</div>
				</div>
			</div>
			<br><br>
		</footer>
		
		<script src="js/jquery-3.2.1.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/jquery.superslides.min.js"></script>
		<script src="js/custom.js"></script>
	</body>
</html>