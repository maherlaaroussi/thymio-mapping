<?php

  $filename = $_GET['filename'];
  $size = 600;
  $original_x = $size / 2;
  $original_y = $size / 2;

  $output = exec("sudo /usr/bin/python3 /var/www/html/python/main.py " .  $filename);

  $myImage = imagecreate($size, $size);

  $myBlack = imagecolorallocate($myImage, 0, 0, 0);
  $myWhite = imagecolorallocate($myImage, 255, 255, 255);

  $output = json_decode($output);

  foreach ($output as $value) {

    $posXF = $value[1] * cos($value[0] / 180 * pi());
    $posYF = $value[1] * sin($value[0] / 180 * pi());
    imageline($myImage, $original_x, $original_y, $posXF, $posYF, $myWhite);

    $posXB = $value[2] * cos(($value[0] + 180) / 180 * pi());
    $posYB = $value[2] * sin(($value[0] + 180) / 180 * pi());
    imageline($myImage, $original_x, $original_y, $posXB, $posYB, $myWhite);

  }

  header( "Content-type: image/png" );
  imagepng($myImage, $filename . ".png");
  header("Content-disposition: attachment; filename=" . $filename . ".png");
  header('Content-Description: File Transfer');
  readfile("" . $filename . ".png");

  imagedestroy($myImage);

?>
