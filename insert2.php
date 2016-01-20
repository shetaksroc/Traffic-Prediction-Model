<?php 

header('Access-Control-Allow-Origin: *');  
header('Access-Control-Allow-Methods: GET, PUT, POST, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Content-Range, Content-Disposition, Content-Description');

 
// include db connect class details
$host="http://manu1193.5gbfree.com:2082";
	$uname="manu1193";
	$pwd='manu123';
	$db="manu1193_trafficdata";

	$con = mysql_connect($host,$uname,$pwd) or die("connection failed");
	mysql_select_db($db,$con) or die("db selection failed");
	
	
//Get values from input form userid:user,Name:nme,address:addr,contact:num,password:pass,busId:bus

$userid = $_POST['stid'];
$Name = $_POST['lat'];
$address = $_POST['long'];
$contact = $_POST['y'];
$password = $_POST['x'];
$busId = $_POST['src'];
$address = $_POST['dest'];
$contact = $_POST['time'];
$password = $_POST['pixel'];
	
	echo($userid);
	
	$sql = "INSERT INTO data(st_id,lat,longitude,y,x,src,dest,time,pixel) VALUES('$userid','$Name','$address','$contact','$password','$busId','$address','$contact','$password')";


$r = mysql_query($sql,$con);

if(!$r)
{
  die('Could not enter data: ' . mysql_error());
}
	mysql_close($con);
 

?>