<?php

 header("Cache-Control: max-age = 604800");
 header("Expires: ".gmdate("D, d M Y H:i:s", time() + 604800)." GMT");
 header("Content-Type: image/jpg");

 $img = 'default.jpg';
 if(file_exists($_GET["img"])) {
    $filename = $_GET["img"];
 }

 $imagick = new Imagick($filename);
 if(isset($_GET["s"])) {
    $imagick->scaleimage($_GET["s"], $_GET["s"]);
 }
 echo $imagick->getImageBlob();

?>
