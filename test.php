<?php

require_once '../phirehose/lib/Phirehose.php';

class MyStreamer extends Phirehose
{
	public function enqueueStatus($status) {
		print $status;
  		//$object = json_decode($status);
		//print_r($object);
		//print_r($object->description);
		//print_r($object->coordinates);
	}
}

$stream = new MyStreamer("roryoung", "opt1pl3x5", Phirehose::METHOD_FILTER);
$stream->setLocations(array(
	array(-14.2,49.8,2.8,60.2)
));
$stream->consume();
