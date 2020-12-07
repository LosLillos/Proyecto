$(document).ready(function(){


 
  var latitude = -16.468252,
  longitude = -65.553275,
  map_zoom = 6;
  
    var is_internetExplorer11= navigator.userAgent.toLowerCase().indexOf('trident') > -1;
    var marker_url = ( is_internetExplorer11 ) ? 'https://www.mediafire.com/convkey/d992/boaao261r6yapedzg.jpg' : 'https://www.mediafire.com/convkey/d992/boaao261r6yapedzg.jpg';
      
    var main_color = '#2d313f',
      saturation_value= -20,
      brightness_value= 5;
  
    var style= [ 
      {
        elementType: "labels",
        stylers: [
          {saturation: saturation_value}
        ]
      },  
      {
        featureType: "road",
        elementType: "geometry.stroke",
        stylers: [
          {visibility: "off"}
        ]
      }, 
      { 
        featureType: "transit", 
        elementType: "geometry.fill", 
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      }, 
      {
        featureType: "poi",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "poi.government",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "poi.sport_complex",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "poi.attraction",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "poi.business",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "transit",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "transit.station",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "landscape",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
        
      },
      {
        featureType: "road",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      },
      {
        featureType: "road.highway",
        elementType: "geometry.fill",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      }, 
      {
        featureType: "water",
        elementType: "geometry",
        stylers: [
          { hue: main_color },
          { visibility: "on" }, 
          { lightness: brightness_value }, 
          { saturation: saturation_value }
        ]
      }
    ];
      
    var map_options = {
          center: new google.maps.LatLng(latitude, longitude),
          zoom: map_zoom,
          panControl: false,
          zoomControl: false,
          mapTypeControl: false,
          streetViewControl: false,
          mapTypeId: google.maps.MapTypeId.ROADMAP,
          scrollwheel: false,
          styles: style,
      }
    var map = new google.maps.Map(document.getElementById('google-container'), map_options);
    
    
    var marker1 = new google.maps.Marker({
      position: new google.maps.LatLng(-17.5732153, -63.1574694),
      map: map,
      visible: true,
    icon: marker_url,
  });
  var marker3 = new google.maps.Marker({
    position: new google.maps.LatLng(-17.768856, -63.129359),
    map: map,
    visible: true,
  icon: marker_url,
  });
  var marker4 = new google.maps.Marker({
    position: new google.maps.LatLng(-17.991408, -67.107528),
    map: map,
    visible: true,
  icon: marker_url,
  });
  var marker5 = new google.maps.Marker({
    position: new google.maps.LatLng(-17.248388, -67.903569),
    map: map,
    visible: true,
  icon: marker_url,
  });
  var marker6 = new google.maps.Marker({
    position: new google.maps.LatLng(-16.546094, -68.228414),
    map: map,
    visible: true,
  icon: marker_url,
  });
  var marker7 = new google.maps.Marker({
  position: new google.maps.LatLng(-11.132816, -68.795140),
  map: map,
  visible: true,
icon: marker_url,
});







  
    function CustomZoomControl(controlDiv, map) {
        var controlUIzoomIn= document.getElementById('zoom-in'),
        controlUIzoomOut= document.getElementById('zoom-out');
        controlDiv.appendChild(controlUIzoomIn);
        controlDiv.appendChild(controlUIzoomOut);
  
      google.maps.event.addDomListener(controlUIzoomIn, 'click', function() {
          map.setZoom(map.getZoom()+1)
      });
      google.maps.event.addDomListener(controlUIzoomOut, 'click', function() {
          map.setZoom(map.getZoom()-1)
      });
    }
  
    var zoomControlDiv = document.createElement('div');
    var zoomControl = new CustomZoomControl(zoomControlDiv, map);
    map.controls[google.maps.ControlPosition.RIGHT_CENTER].push(zoomControlDiv);
    
    
      
  
        /* AUTHOR LINK */
       $('.about-me-img').hover(function(){
              $('.authorWindowWrapper').stop().fadeIn('fast').find('p').addClass('trans');
          }, function(){
              $('.authorWindowWrapper').stop().fadeOut('fast').find('p').removeClass('trans');
          });
    
    
    
    
  });