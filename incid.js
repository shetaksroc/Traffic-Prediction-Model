function initialize() {
   /*-- fixed init vars */
    var baseLat = 12.971599;
    var baseLong = 77.594563;

    var OffsetLat = 10.4;
    var OffsetLong = 10.75;

    /*-- South Latitude, West Longitude, North Latitude, East Longitude based on the offset to calc the initial rectangle */

    var SouthLat = baseLat - OffsetLat;
    var WestLong = baseLong - OffsetLong;
    var NorthLat = baseLat + OffsetLat;
    var EastLong = baseLong + OffsetLong;

    var laukizuzen_muga_hasiera = SouthLat + "," + WestLong + "," + NorthLat + "," + EastLong;

//    console.log(laukizuzen_muga_hasiera);         
    
    function istilu_eskuratu(laukizuzen_muga) {
     
    /*-- Custom Google Maps Init */

    /*-- Map Styling Options */

    var MY_MAPTYPE_ID = 'custom_style';

    var featureOpts = [
  {
    "featureType": "landscape",
    "stylers": [
      { "saturation": -100 },
      { "invert_lightness": true }
    ]
  },
  {
    featureType: "road",
    elementType: "labels",
    stylers: [
                { "visibility": "off" }
		
    ]
  },{
    "featureType": "poi",
    "stylers": [
           { "visibility": "off" }
    ]
  },{
    "featureType": "transit",
    "stylers": [
      { "visibility": "off" }
    ]
  },{
    "featureType": "water",
    "stylers": [
    { "visibility": "off" }
    ]
  },{
    "featureType": "administrative",
    "stylers": [
            { "visibility": "off" }
    ]
  },{
    "featureType": "road",
    "stylers": [
             { "visibility": "off" }
    ]
  }
];

         
    /*-- Map General Options */

    var mymapOptions = {
        zoom:12,
        center: new google.maps.LatLng(baseLat, baseLong),

        mapTypeControlOptions: {
            mapTypeIds: [MY_MAPTYPE_ID]
            /*,style: google.maps.MapTypeControlStyle.DROPDOWN_MENU*/
        },

        mapTypeControl: false,
        navigationControl: true,
        panControl: false,
        streetViewControl: false,
        mapTypeId: MY_MAPTYPE_ID
    };

    /*-- init map */

    var map;

    map = new google.maps.Map(document.getElementById("map"), mymapOptions);

    /*-- apply styling to map */

    var styledMapOptions = {
        name: 'Custom Style'
    };

    var customMapType = new google.maps.StyledMapType(featureOpts, styledMapOptions);

    map.mapTypes.set(MY_MAPTYPE_ID, customMapType);

    /*-- load the live traffic layer */

    var trafficLayer = new google.maps.TrafficLayer();
    trafficLayer.setMap(map);
    //console.log(trafficLayer);
    
    /*-- Define the rectangle and set its editable property to true. */
    //SouthLat + "," + WestLong + "," + NorthLat + "," + EastLong;
    
    var rectangle;
    
    // some ofset to fake the rectangle area and make it slightly bigger
    var aumento=0.05;
    
    rectangle = new google.maps.Rectangle({
        bounds: new google.maps.LatLngBounds(
        new google.maps.LatLng(SouthLat-aumento, WestLong-aumento),
        new google.maps.LatLng(NorthLat+aumento, EastLong+aumento)
        ),
        strokeColor: '#f00',
        strokeOpacity: 0.5,
        strokeWeight: 2,
        fillColor: '#fff',
        fillOpacity: 0,
        /*editable: true,
        draggable: true,*/
        map: map
    });
        
        /*-- reset incident list */

        $('.toggle-incident-grp').empty();

        /*-- get all the incidents from microsoft virtual earth traffic service */

        var istilu_key = "ArO32ckVJYpJCDs_5WKAN8ywK66lEVJ6_YOa_V3uegHGyK9v_xqMKgzqwk_uynPi";

        var istilu_url = "http://dev.virtualearth.net/REST/v1/Traffic/Incidents/" + laukizuzen_muga + "?output=json&key=ArO32ckVJYpJCDs_5WKAN8ywK66lEVJ6_YOa_V3uegHGyK9v_xqMKgzqwk_uynPi";

        //console.log(istilu_url);

        var infoWindow = new google.maps.InfoWindow({
            maxWidth: 200
        });

        //*-- when marker is clicked */
        
        var onMarkerClick = function () {
            var marker = this;
            //console.log(marker);
            infoWindow.setContent(marker.title);
            infoWindow.open(map, marker);
        };
        
          
        
        
        /*-- ajax JSONP dataType request */

        $.ajax({
            type: 'GET',
            url: istilu_url,
            dataType: "jsonp",
            timeout: 5000,
            jsonp: 'jsonp',

            success: function (parsed_json) {

                if (parsed_json !== "") {

                    console.log(parsed_json);               

                    /*-- Define custom count to store the markers array */
				

                    incidentNum = 0;
                    
                    myIcon = [];
                    
                    marker = [];

                    /*-- the loop based on the number of resourceSets found in the JSONP structure */
					
                    $.each(parsed_json.resourceSets[0].resources, function (i, el) {

                        /*-- Custom autoincrement based on each resourceSet */

                        incidentNum++;

                        var markerId = incidentNum;

                        /*-- Customs vars */
                        
                        var startDate = el.start;
                        var endDate = el.end;
                        
                        var desc1= el.description.split(' - ').slice(0, 1);
                        var whot= el.description.split(' - ').slice(1);   
                        
                        myIcon[markerId] = new google.maps.MarkerImage(getIncidentIcon(el.type), null, null, null, new google.maps.Size(32,32));
                        
                        marker[markerId] = new google.maps.Marker({
                            position: new google.maps.LatLng(el.point.coordinates[0], el.point.coordinates[1]),
                            map: map,
                            //title: incidentNum + ' ' + "<b>"+desc1+"</b><br/>"+whot,
                            title:  "<b>"+desc1+"</b><br/>"+
                                    whot+ "<br />" +
                                    "<a class='btn-details' href=#" + incidentNum + ">Go To List Item</a>"
                            ,
                            icon: myIcon[markerId]
                        });

                        google.maps.event.addListener(marker[markerId], 'click', onMarkerClick);

                        /*-- Render list of incidents */                       

                        $('.toggle-incident-grp').append(
                            
                        "<a id=" + incidentNum + "/>"+
                            
                        "<label class='toggle-incident-btn' id='" + incidentNum + "'>" +
                            
                        "<input type='radio' name='incident-group' />" +
                        
                        "<div class='leftContent'>" +
                            "<span class='iconType'><img src=" + getIncidentIcon(el.type) + " /></span>" +
                            "<span class='descType'>"+getIncidentDescription(el.type)+"</span>" +
                            "<span class='roadStatus'><img src=" + getRoadConditionIcon(el.roadClosed) + " /></span>" +
                        "</div>" +
                        
                        "<div class='rightContent'>" +                            
                            "<span class='whatIncident'>"+ whot  + "</span>" +
                            "<span class='whereIncident'>" + desc1 + "</span>" +
                            "<span class='timeIncidentStart'>"+ getdhm(startDate) +"</span>" +
                            "<span class='timeIncidentEnd'>"+ getdhm(endDate) +"</span>" +
                            
                        "</div>" +
                            
                        "</label>");

                    });

                    /*-- listener to show the incident on the map when clicked on the element on the list  */

                    $('.toggle-incident-btn').on('click', '#' [$(this).attr('id')], function () {
                        google.maps.event.trigger(marker[$(this).attr('id')], 'click');
                        //map.panTo(new google.maps.LatLng(el.point.coordinates[0], el.point.coordinates[1]));
                        //map.setZoom(13);
                        console.log(marker[$(this).attr('id')])
                    });
                    
                    /*-- Toggle incidents init */
    
                    $(".toggle-incident-btn input[type=radio]").addClass("visuallyhidden");
    
                    $(".toggle-incident-btn input[type=radio]").change(function () {
                      // console.log($(this).attr("name"));
                        if ($(this).attr("name")) {
                            $(this).parent().addClass("active-incident").siblings().removeClass("active-incident");
                            
                        } else {
                            $(this).parent().toggleClass("active-incident");
                        }                       

                       scrollToAnchor('Top');
                        
                    });
                    
                    $('#tools .numberOfincidents').html(incidentNum +" Incidents");
                    
                }

                /*-- Custom Ajax error message if call suceeds but no data or error is found*/

                else {

                    console.log('Sorry Traffic info not available');
                }
            },

            /*-- OOB Ajax Error */

            error: function (parsedjson, textStatus, errorThrown) {

                if (errorThrown) {
                    console.log('Sorry, Ajax Error! ' + errorThrown);
                    //console.log("parsedJson:" + JSON.stringify(parsedjson));
                    console.log("errorStatus:" + textStatus);
                    console.log("errorThrown:" + errorThrown);
                } else {
                    console.log('Sorry, Unknown Ajax Error!');
                }

            }
        });
    }

    /*-- DATE STUFF */
    /*-- Refactor the JavaScript default Date() object to shorten the day of the week */

    Date.prototype.getDayName = function () {
        var d = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        return d[this.getDay()];
    };

    /*-- get the JSON Epoch Unix time and transfor it to GMTString */

    function getdhm(msUnixEpochTime) {
        var msDateTrimStartEnd = new Date(parseInt(msUnixEpochTime.substr(6), 10));
        theDate = new Date(msDateTrimStartEnd);
        dateString = theDate.toGMTString();
        return dateString;
    }
    
    /*-- Find the Icon based on Type of incident */
    
    function getIncidentIcon(incidentCode){
            var baseIconURL="https://dl.dropboxusercontent.com/u/65863525/images/traffic/";
    switch (incidentCode) {
        case 1:
            return baseIconURL+"itype_1_Accident.png";
        case 2:
            return baseIconURL+"itype_2_Congestion.png";
        case 3:
            return baseIconURL+"itype_3_DisabledVehicle.png";
        case 4:
            return baseIconURL+"itype_4_MassTransit.png";
        case 5:
            return baseIconURL+"itype_5_Miscellaneous.png";
        case 6:
            return baseIconURL+"itype_6_OtherNews.png";
        case 7:
            return baseIconURL+"itype_7_PlannedEvent.png";
        case 8:
            return baseIconURL+"itype_8_RoadHazard.png";
        case 9:
            return baseIconURL+"itype_9_Construction.png";
        case 10:
            return baseIconURL+"itype_10_Accident.png";
        case 11:
            return baseIconURL+"itype_11_Weather.png";
        case "":
            return baseIconURL+"itype_10_Alert.png";
        default:
            return baseIconURL+"itype_10_Alert.png";
    }        
    }
    
     function getIncidentDescription(incidentCode){
    switch (incidentCode) {
        case 1:
            return "Accident";
        case 2:
            return "Congestion";
        case 3:
            return "Disabled Vehicle";
        case 4:
            return "Mass Transit";
        case 5:
            return "Misc.";
        case 6:
            return "Other News";
        case 7:
            return "Planned Event";
        case 8:
            return "Road Hazard";
        case 9:
            return "Construction";
        case 10:
            return "Alert";
        case 11:
            return "Weather hazard";
        case "":
            return "Miscellaneous";
        default:
            return "Miscellaneous";
    }        
    }
    
    function getRoadConditionIcon(roadConditionBool){
            var baseIconURL="https://dl.dropboxusercontent.com/u/65863525/images/traffic/";
    switch (roadConditionBool) {
        case "true":
            return baseIconURL+"RoadClosed.png";
        case "false":
            return baseIconURL+"RoadOpen.png";
        default:
            return baseIconURL+"RoadOpen.png";
    }        
    }
    
    function scrollToAnchor(aid){
    var aTag = $("a[name='"+ aid +"']");
    $('html,body').animate({scrollTop: aTag.offset().top},'slow');
}   

    /*-- Init the main function with the default declared coords */

    istilu_eskuratu(laukizuzen_muga_hasiera);

    $( ".btn-ResetMap" ).click(function() {
    istilu_eskuratu(laukizuzen_muga_hasiera);
});
    
     $( ".btn-GoToList" ).click(function() {
     scrollToAnchor('List');
});
    
}