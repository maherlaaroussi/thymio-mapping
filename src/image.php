<?php

  header( "Content-type: image/png" );

  $myImage = imagecreate(600, 600);


  $myBlack = imagecolorallocate($myImage, 0, 0, 0);
  $myWhite = imagecolorallocate($myImage, 255, 255, 255);

  imageline($myImage, 15, 35, 120, 60, $myBlack);

  imagepng($myImage);
  imagedestroy( $myImage );

?>
