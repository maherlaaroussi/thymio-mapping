<?php

  $filename = $_GET['filename'];
  $path_image = $filename . ".png";
  $size = 600;
  $original_x = $size / 2;
  $original_y = $size / 2;
  $resize = 5;

  $output = exec("sudo /usr/bin/python3 /var/www/html/python/main.py " .  $filename);

  echo $output;

?>
