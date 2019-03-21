<?php

header ("Content-type: image/png");


$im = @ImageCreate (100, 200)
or die ("Cannot Initialize new GD image stream");

$background_color = ImageColorAllocate ($im, 224, 234, 234);

$text_color = ImageColorAllocate ($im, 233, 14, 91);

 imageline ($im, 0, 0, 100, 200, $text_color);
 imageline ($im, 100, 0, 0, 200, $text_color);

ImagePng ($im);

?>
