<?php
// database connection code
if(isset($_POST['save']))
{
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','mushroomdata_input');

// get the post records

$CapShape = $_POST['CapShape'];
$CapSurface = $_POST['CapSurface'];
$CapColor = $_POST['CapColor'];
$Bruises = $_POST['Bruises'];
$Ordor = $_POST['Ordor'];
$GillAttachment = $_POST['GillAttachment'];
$GillSpacing = $_POST['GillSpacing'];
$GillSize = $_POST['GillSize'];
$GillColor = $_POST['GillColor'];
$StalkShape = $_POST['StalkShape'];
$StalkRoot = $_POST['StalkRoot'];
$StalkSurfaceAboveRing = $_POST['StalkSurfaceAboveRing'];
$StalkSurfaceBelowRing = $_POST['StalkSurfaceBelowRing'];
$StalkColorAboveRing = $_POST['StalkColorAboveRing'];
$StalkColorBelowRing = $_POST['StalkColorBelowRing'];
$VeilColor = $_POST['VeilColor'];
$RingNumber = $_POST['RingNumber'];
$RingType = $_POST['RingType'];
$SporePrintColor = $_POST['SporePrintColor'];
$Population = $_POST['Population'];
$Habitat = $_POST['Habitat'];

// database insert SQL code
$sql = "INSERT INTO `input_data` (`Id`, `Cap Shape`, `Cap Surface`, `Cap Color`, `Bruises`, `Ordor`, `Gill Attachment`, `Gill Spacing`, `Gill Size`, `Gill Color`, 
`Stalk Shape`, `Stalk Root`, `Stalk Surface Above Ring`, `Stalk Surface Below Ring`, `Stalk Color Above Ring`, `Stalk Color Below Ring`, `Veil Color`, `Ring Number`, 
`Ring Type`, `Spore Print Color`, `Population`, `Habitat`) 
VALUES ('0', '$CapShape', '$CapSurface', '$CapColor', '$Bruises', '$Ordor', '$GillAttachment', '$GillSpacing', '$GillSize', '$GillColor', '$StalkShape', '$StalkRoot', 
'$StalkSurfaceAboveRing', '$StalkSurfaceBelowRing', '$StalkColorAboveRing', '$StalkColorBelowRing', '$VeilColor', '$RingNumber', 
'$RingType', '$SporePrintColor', '$Population', '$Habitat')";

// insert in database 
$rs = mysqli_query($con, $sql);
if($rs)
{
	echo "Input Records Inserted";
}
}
else
{
	echo "Are you a genuine visitor?";
	
}
?>