<!DOCTYPE html>
<html class="full" lang="en">
<!-- Make sure the <html> tag is set to the .full CSS class. Change the background image in the full.css file. -->

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Full - Start Bootstrap Template</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/full.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="index.html">Locate</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="#">Rate</a>
                    </li>
                    <li>
                        <a href="#">Services</a>
                    </li>
                    <li>
                        <a href="#">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

     <div class="container">
            <div class="row">
                <div class="col-md-6 col-sm-12">
                    <h1>Thanks For your review</h1>

    		<?php

    		$servername = "localhost";
    		$username = "root";
    		$password = "code4good";
    		$dbname = "team4";

    		$streetname = $_POST["STREETNAME"];
    		$addressnumber = $_POST["ADDRESSNUMBER"];
    		$zip = $_POST["ZIP"];
    		$locationname = $_POST["LOCATIONNAME"];
    		$rating = $_POST["RATING"];


    		$conn = new mysqli($servername, $username, $password, $dbname);

    		if ($conn->connect_error) {
    		   die("Connection failed: " . $conn->connect_error);
    		}


    		



    		$sql = "INSERT INTO locations (STREETNAME, ADDRESSNUMBER, ZIP, LOCATIONNAME, RATING) VALUES ('$streetname', $addressnumber, $zip, '$locationname', $rating)";

    		if ($conn->query($sql) === TRUE) {
      		  echo "New record created successfully";
    		} else {
    		    echo "Error: " . $sql . "<br>" . $conn->error;
    		}


    		$conn->close();
    		?>


                </div>
            </div>
            <!-- /.row -->
        </div>
        <!-- /.container -->

    <!-- Put your page content here! -->
    <div id="map" style="width: 100%; height: 94%; position: absolute; vertical-align:middle;">
        <script async defer
                src="https://maps.googleapis.com/maps/api/js?key=AIzaSyClf55i7ai_BLWi1C__3gJsbT6CsLNuzV4&callback=initMap">
        </script>
    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>
