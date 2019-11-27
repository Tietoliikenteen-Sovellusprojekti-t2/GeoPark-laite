<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Rasp to Database</title>
</head>
	<body>
	Lisaa Tietokantaan:
	<form method="post" action="index.php">
		<input type="submit" value="lisaa" name="on">
	</form>
	<?php
	//$semode = shell_exec("python /home/pi/GeoPark-laite/koodit/Testikoodit/TiedonLisaysTietokantaan_v1.py");
	//echo "galloo";
	if(isset($_POST['on'])){
		$latettaa = shell_exec('python /home/pi/GeoPark-laite/koodit/Testikoodit/TiedonLisaysTietokantaan_v1.py');
		echo "lahetettiin!";
		echo $latettaa;
	}
	?>
	</body>
</html>
