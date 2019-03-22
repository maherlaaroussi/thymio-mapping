<?php

  $filename = $_GET['filename'];
  $size = 600;
  $original_x = $size / 2;
  $original_y = $size / 2;

  $output = exec("sudo /usr/bin/python3 /var/www/html/python/main.py " .  $filename);

  $myImage = imagecreate($size, $size);

  $myBlack = imagecolorallocate($myImage, 0, 0, 0);
  $myWhite = imagecolorallocate($myImage, 255, 255, 255);
  /*
  $handle = fopen("data/" . filename . ".txt", "r");
  $values = "";

  if ($handle) {
    while (($line = fgets($handle)) !== false) {
      $values = explode(":", $line);
      $x = $values[1] * cos(($values[0] + 180) / 180. * pi())
      $y = $values[2] * sin(($values[0] + 180) / 180. * pi())
      imageline($myImage, $original_x, $original_y, $x, $y, $myWhite);
    }
  fclose($handle);

  } else {
      imageline($myImage, $original_x, $original_y, 200, 200, $myWhite);
  }
  */
  header( "Content-type: image/png" );
  imagepng($myImage, $filename . ".png");
  header("Content-disposition: attachment; filename=" . $filename . ".png");
  header('Content-Description: File Transfer');
  readfile("" . $filename . ".png");

  imagedestroy($myImage);

?>
