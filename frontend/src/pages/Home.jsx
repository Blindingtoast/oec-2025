import React from "react";
import NavDock from "@/components/ui/nav-dock";
import { GoogleMap, useJsApiLoader, Marker } from "@react-google-maps/api";
import { useEffect, useState } from "react";

const mapMarkers = (report) => ({ lat: report.lat, lng: report.long });

const Home = () => {
	const [center, setCenter] = useState(null);
	const [markerPositions, setMarkerPositions] = useState([]);
	const [locationsSocket, setLocationsSocket] = useState(null);

	useEffect(() => {
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(success, error);
		} else {
			console.log("Geolocation not supported");
		}
		console.log("Fetching locations", markerPositions);
		// get json from api/reports/location and set markerPositions
		fetch("/api/reports/locations")
			.then((response) => response.json())
			.then((data) => {
				setMarkerPositions(data.map(mapMarkers))
			});
		// open a websocket that will give us any new markers that show up
		setLocationsSocket(new WebSocket("/api/updates/reports"));
		locationsSocket.addEventListener("message", (data) => {
			console.log("got some new markers");
			setMarkerPositions(markerPositions.concat(data.map(mapMarkers)));
		});
	}, []);

	function success(position) {
		const latitude = position.coords.latitude;
		const longitude = position.coords.longitude;
		setCenter({ lat: latitude, lng: longitude });
		console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
	}

	function error() {
		console.log("Unable to retrieve your location");
	}

	return (
		<>
			<NavDock />
			<div className="flex justify-center items-center">
				<Map center={center} markerPositions={markerPositions} />
			</div>
		</>
	);
};

const containerStyle = {
	width: "90vw",
	height: "90vh",
};

function Map({ center, markerPositions }) {
	const { isLoaded } = useJsApiLoader({
		id: "google-map-script",
		googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
	});

	const [map, setMap] = React.useState(null);

	const onLoad = React.useCallback(function callback(map) {
		const bounds = new window.google.maps.LatLngBounds(center);
		map.fitBounds(bounds);

		setMap(map);
	}, []);

	const onUnmount = React.useCallback(function callback(map) {
		setMap(null);
	}, []);

	return isLoaded ? (
		<GoogleMap
			mapContainerStyle={containerStyle}
			center={center}
			zoom={10}
			onLoad={onLoad}
			onUnmount={onUnmount}
		>
			{markerPositions.map((position, index) => (
				<Marker key={index} position={position} />
			))}
		</GoogleMap>
	) : (
		<></>
	);
}

export default Home;
