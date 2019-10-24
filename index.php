<!DOCTYPE html>
<html>
  <head>
    <title>Calcul Routier</title>
  </head>
  <body>


  <?php
$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://distanceto.p.rapidapi.com/get');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
	'car' => 'false',
	'foot' => 'false',
	'route' => '{"t":"Hamburg"}]'
)));

$request->setHeaders(array(
	'x-rapidapi-host' => 'distanceto.p.rapidapi.com',
	'x-rapidapi-key' => '29c34300f0mshab3f54180151872p1b2b8djsn4015c6519010'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();
?>



  </body>
</html>