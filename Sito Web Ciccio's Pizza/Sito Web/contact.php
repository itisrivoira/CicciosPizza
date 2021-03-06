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
							<li class="nav-item active"><a class="nav-link" href="contact.php">Contattaci</a></li>
							<li class="nav-item"><a class="nav-link" href="login.php">Login</a></li>
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
						<h1>Contattaci</h1>
					</div>
				</div>
			</div>
		</div>

		<div class="contact-box">
			<div class="container">
				<div class="row">
					<div class="col-lg-12">
						<div class="heading-title text-center"> <br>
							<h2>Domande</h2>
							<p>Completa il form per inviarci una domanda</p>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="col-lg-12">
						<form method="post" id="contactForm" action="sendmail.php">
							<div class="row">
								<div class="col-md-12">
									<div class="form-group">
										<input type="text" placeholder="Nome" class="form-control" id="name" name="name"  required data-error="Please enter your name">
										<div class="help-block with-errors"></div>
									</div>                                 
								</div>
								<div class="col-md-12">
									<div class="form-group">
										<input type="text" placeholder="Email" class="form-control" id="email"  name="email" required data-error="Please enter your email">
										<div class="help-block with-errors"></div>
									</div> 
								</div>
								<div class="col-md-12">
									<div class="form-group">
										<textarea placeholder="Messaggio" class="form-control" id="message" name="message" rows="4" required data-error="Write your message"></textarea>
										<div class="help-block with-errors"></div>
									</div><br>
								</div><br>
								<div class="col-md-12">
									<div class="submit-button text-center">
										<button class="btn btn-common" id="submit" type="submit">Invia il messaggio</button>
									</div>
								</div>
							</div>            
						</form>
					</div>
				</div>
			</div>
		</div>

		<br><br>

		<footer class="footer-area bg-f">
			<div class="container">
				<div class="row">
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