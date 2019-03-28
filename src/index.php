<!DOCTYPE html>
<html lang="fr">
<head>
	<title>Thymio Mapping</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/iconic/css/material-design-iconic-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>

	<div id="login" class="limiter">
		<div class="container-login100">
			<div class="wrap-login100 p-t-85 p-b-20">

					<span id="titre" class="login100-form-title p-b-70">
						Thymio Mapping
					</span>

					<span id="image" class="login100-form-image">
							<img id ="loading" src="" alt="Loading" hidden>
						<img id ="blueprint" src="images/mapping.jpg" alt="Mapping">
					</span>

					<div class="container-login100-form-btn">
						<button id="mapping" class="login100-form-btn" type="button">
							Scanner
						</button>
					</div>

			</div>
		</div>
	</div>

	<div id="profil" class="limiter" hidden>

		<div class="container-login100">
			<div class="wrap-login100 p-t-85 p-b-20">

				<form class="login100-form validate-form">

					<span id="profilindex" class="login100-form-title p-b-70">
					</span>

					<div class="container-login100-form-btn">
						<button id="btn-infos" class="login30-form-btn" type="button">
							Informations
						</button>
						<button id="btn-dossier" class="login30-form-btn" type="button">
							Dossier
						</button>
						<button id="btn-edt" class="login30-form-btn" type="button">
							EDT
						</button>
					</div>

					<span class="login100-form-avatar">
						<img src="images/avatar-01.jpg" alt="AVATAR">
					</span>

					<div id="informations" data-index="infos">

						<div class="wrap-input100 validate-input m-t-85 m-b-35" data-validate = "Entez votre numéro étudiant">
							<span data-placeholder="Nom">Nom</span>
							<input id="profilnom" class="input100" type="text" name="nom" value="" disabled>
						</div>

						<div class="wrap-input100 validate-input m-b-50" data-validate="Entrez votre mot de passe">
							<span data-placeholder="Prénom">Prénom</span>
							<input id="profilprenom" class="input100" type="text" name="prenom" value="" disabled>
						</div>

						<div class="wrap-input100 validate-input m-b-50" data-validate="Entrez votre mot de passe">
							<span data-placeholder="Birthday">Date de naissance</span>
							<input id="profilbirthday" class="input100" type="text" name="birthday" value="" disabled>
						</div>

				</div>

				<div id="dossier" data-index="dossier" hidden>

					<div class="wrap-input100 validate-input m-t-85 m-b-35" data-validate = "Entez votre numéro étudiant">
						<span data-placeholder="Numéro">Numéro étudiant</span>
						<input id="profilusername" class="input100" type="text" name="username" value="" disabled>
					</div>

					<div class="wrap-input100 validate-input m-b-50" data-validate="Entrez votre mot de passe">
						<span data-placeholder="INE">INE</span>
						<input id="profiline" class="input100" type="text" name="ine" value="" disabled>
					</div>

					<div class="wrap-input100 validate-input m-b-50" data-validate="Entrez votre mot de passe">
						<span data-placeholder="Formation">Formation</span>
						<input id="profilformation" class="input100" type="text" name="formation" value="" disabled>
					</div>

			</div>

				</form>

			</div>
		</div>
	</div>


	<div id="dropDownSelect1"></div>

<!--===============================================================================================-->
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/animsition/js/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/daterangepicker/moment.min.js"></script>
	<script src="vendor/daterangepicker/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="vendor/countdowntime/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

<script src="js/pace.min.js"></script>

	<script>

	const path = "scan.php";

	$(document).ready(function() {

		$("#mapping").click(function() {

			var date = new Date();
			var timestamp = date.getTime();

			console.log("Lancement du scan ... " + timestamp);

			$.ajax({
				url: path,
				type: "get",
				data: {filename: timestamp},
				success: function(response) {
					$("#blueprint").hide();
					$('#image').html('<img src="' + timestamp + '.png" ></img>');
				}
			});

		});


		$(document).keypress(function(e) {
			if(e.which == 13) {
				$("#mapping").click();
			}

		});


	});
	</script>

</body>
</html>
