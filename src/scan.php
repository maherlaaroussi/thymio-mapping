<?php

  $filename = $_GET['filename'];
  $path_image = $filename . ".png";


  $output = exec("sudo /usr/bin/python3 /var/www/html/python/main.py " .  $filename);
  $output = json_decode($output);

  $maxSize = 0;

  foreach ($output as $value) {
    if ($value[1] > $maxSize) { $maxSize = $value[1]; }
    if ($value[2] > $maxSize) { $maxSize = $value[2]; }
  }

  $resize = 4;
  $size = $maxSize * $resize;
  $original_x = $size / 2;
  $original_y = $size / 2;
  $xEchelle = $size * 0.05;
  $yEchelle = $size * 0.95;

  $myImage = imagecreate($size, $size);

  $myBlack = imagecolorallocate($myImage, 0, 0, 0);
  $myWhite = imagecolorallocate($myImage, 255, 255, 255);
  
  imagesetthickness($myImage, 2);

  $i = 0;
  $xF_old = 0;
  $yF_old = 0;
  $xB_old = 0;
  $yB_old = 0;

  foreach ($output as $value) {

    $xF_old = $posXF;
    $yF_old = $posYF;
    if ($value[1] != 0) {
      $posXF = $value[1] * $resize * cos($value[0] / 180 * pi());
      $posXF = $original_x + round($posXF, 2);
      $posYF = $value[1] * $resize * sin($value[0] / 180 * pi());
      $posYF = $original_y + round($posYF, 2);
      if ($i != 0) {
        imageline($myImage, $xF_old, $yF_old, $posXF, $posYF, $myWhite);
      }
    }

    $xB_old = $posXB;
    $yB_old = $posYB;
    if ($value[1] != 0) {
      $posXB = $value[2] * $resize * cos(($value[0] + 180) / 180 * pi());
      $posXB = $original_x + round($posXB, 2);
      $posYB = $value[2] * $resize * sin(($value[0] + 180) / 180 * pi());
      $posYB = $original_y + round($posYB, 2);
      if ($i != 0) {
        imageline($myImage, $xB_old, $yB_old, $posXB, $posYB, $myWhite);
      }
    }

    $i++;

  }

  // Echelle
  imageline($myImage, $xEchelle, $yEchelle, $xEchelle, ($yEchelle - $resize * 10), $myWhite);
  imageline($myImage, $xEchelle, $yEchelle, ($xEchelle + $resize * 10), $yEchelle, $myWhite);

  header( "Content-type: image/png" );
  imagepng($myImage, $path_image);
  header("Content-disposition: attachment; filename=" . $path_image);
  header('Content-Description: File Transfer');
  readfile("" . $path_image);

  imagedestroy($myImage);

?>
