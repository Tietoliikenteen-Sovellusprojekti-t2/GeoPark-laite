

<!DOCTYPE html>
<html>
<head>
  <title>test</title>
</head>
<body>
  <table>
    <tr>
      <th>nro</th>
      <th>lat</th>
      <th>lng</th>
    </tr>
    <?php
  foreach ($userArray as $key => $value) {
    
    echo"<tr>
      <td>".$value['Nro']."</td>
      <td>".$value['lat']."</td>
      <td>".$value['lng']."</td>
      </tr>";
      
    }
    ?>
    </table>
  </body>
  </html>
  
<!DOCTYPE html>
<html>

  <head>
    <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 400px;  /* The height is 400 pixels */
        width: 100%;  /* The width is the width of the web page */
        background-color: grey;
       }
    </style>
  </head>

  <body>
    <h3>GeoPark</h3>
    <!--The div element for the map -->
    <div id="map"></div>
    <script>
// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: 64.995029, lng: 25.5096322};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}
    </script>
    <!--Load the API from the specified URL
    * The async attribute allows the browser to render the page while the API loads
    * The key parameter will contain your own API key (which is not needed for this tutorial)
    * The callback parameter executes the initMap() function
    -->
     <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAT46xZAA3LSvTN81fv09whGe6SF81oi5I&callback=initMap"
    async defer></script>
  <body>

</html>