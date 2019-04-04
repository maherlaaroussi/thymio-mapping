<?php

  $filename = $_GET['filename'];
  $path_image = $filename . ".png";
  $size = 600;
  $original_x = $size / 2;
  $original_y = $size / 2;
  $resize = 4;

  $output = exec("sudo /usr/bin/python3 /var/www/html/python/main.py " .  $filename);

  $myImage = imagecreate($size, $size);

  $myBlack = imagecolorallocate($myImage, 0, 0, 0);
  $myWhite = imagecolorallocate($myImage, 255, 255, 255);
  imagesetthickness($myImage, 2);

  $output = json_decode($output);
  $positions = [];

  $i = 0;
  $xF_old = 0;
  $yF_old = 0;
  $xB_old = 0;
  $yB_old = 0;

  foreach ($output as $value) {

    $xF_old = $posXF;
    $yF_old = $posYF;
    $posXF = $value[1] * $resize * cos($value[0] / 180 * pi());
    $posXF = $original_x + round($posXF, 2);
    $posYF = $value[1] * $resize * sin($value[0] / 180 * pi());
    $posYF = $original_y + round($posYF, 2);

    $xB_old = $posXB;
    $yB_old = $posYB;
    $posXB = $value[2] * $resize * cos(($value[0] + 180) / 180 * pi());
    $posXB = $original_x +$positions.push([posXF, posYF]);
    $positions.push([posXB, posYB]); round($posXB, 2);
    $posYB = $value[2] * $resize * sin(($value[0] + 180) / 180 * pi());
    $posYB = $original_y + round($posYB, 2);

    imageline ($myImage , $xF_old, $yF_old, $xF_old, $xF_old, $MyWhite);
    imageline ($myImage , $xB_old, $xB_old, $xB_old, $xB_old, $MyWhite);

    $i++;

  }

  header( "Content-type: image/png" );
  imagepng($myImage, $path_image);
  header("Content-disposition: attachment; filename=" . $path_image);
  header('Content-Description: File Transfer');
  readfile("" . $path_image);

  imagedestroy($myImage);

?>
