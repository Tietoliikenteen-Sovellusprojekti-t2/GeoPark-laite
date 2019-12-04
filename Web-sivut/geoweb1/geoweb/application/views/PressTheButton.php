<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>GPS-tietojen lisääminen tietokantaan</title>
</head>
	<body>
	Lisää tietokantaan:
	<form method="post" antion="PressTheButton.php">
		<input type="submit" value="lisää" name="on">
	</form>
	<?php
	if(isset($_POST['on'])){
		$laheta = shell_exec('python /home/ubuntu/git/GeoPark-laite/mqtt_publisher.py');
		echo $laheta;
		echo "Lähetettii!";
	}
	?>
	</body>
</html>