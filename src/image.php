<?php

  header( "Content-type: image/png" );
  
  $myImage = imagecreate( 200, 100 );

  $myGray = imagecolorallocate( $myImage, 204, 204, 204 );
  $myBlack = imagecolorallocate( $myImage, 0, 0, 0 );
  imageline( $myImage, 15, 35, 120, 60, $myBlack );

  imagepng( $myImage );

  imagedestroy( $myImage );

?>
