<?php

  $filename = $_GET['filename'];

  /* $output = exec("sudo /usr/bin/python3 /var/www/html/python/main.py " .  $filename); */

  $myImage = imagecreate(600, 600);

  $myBlack = imagecolorallocate($myImage, 0, 0, 0);
  $myWhite = imagecolorallocate($myImage, 255, 255, 255);

  imageline($myImage, 0, 0, 500, 500, $myWhite);

  header( "Content-type: image/png" );
  imagepng($myImage, $filename . ".png");
  header("Content-disposition: attachment; filename=" . $filename . ".png");
  header('Content-Description: File Transfer');
  readfile("" . $filename . ".png");

  imagedestroy($myImage);

?>
