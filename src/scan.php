<?php

  $filename = $_GET['filename'];
  $path_image = "maps/" . $filename . ".png";
  $size = 400;
  $original_x = $size / 2;
  $original_y = $size / 2;
  $resize = 4;

  $output = exec("sudo /usr/bin/python3 /var/www/html/python/main.py " .  $filename);

  $myImage = imagecreate($size, $size);

  $myBlack = imagecolorallocate($myImage, 0, 0, 0);
  $myWhite = imagecolorallocate($myImage, 255, 255, 255);
  imagesetthickness($myImage, 2);

  $output = json_decode($output);

  foreach ($output as $value) {

    $posXF = $value[1] * $resize * cos($value[0] / 180 * pi());
    $posXF = $original_x + round($posXF, 2);
    $posYF = $value[1] * $resize * sin($value[0] / 180 * pi());
    $posYF = $original_y + round($posYF, 2);
    imageline($myImage, $original_x, $original_y, $posXF, $posYF, $myWhite);

    $posXB = $value[2] * $resize * cos(($value[0] + 180) / 180 * pi());
    $posXB = $original_x + round($posXB, 2);
    $posYB = $value[2] * $resize * sin(($value[0] + 180) / 180 * pi());
    $posYB = $original_y + round($posYB, 2);
    imageline($myImage, $original_x, $original_y, $posXB, $posYB, $myWhite);

  }

  header( "Content-type: image/png" );
  imagepng($myImage, $path_image);
  header("Content-disposition: attachment; filename=" . $path_image);
  header('Content-Description: File Transfer');
  readfile("" . $filename);

  imagedestroy($myImage);

?>
