import React from "react";
import NavDock from "@/components/ui/nav-dock";
import { GoogleMap, useJsApiLoader } from "@react-google-maps/api";

const Home = () => {
	return (
		<>
			<NavDock />
			<div className="flex justify-center items-center">
				<Map />
			</div>
		</>
	);
};

const containerStyle = {
	width: "90vw",
	height: "90vh",
};

const center = {
	lat: -3.745,
	lng: -38.523,
};

function Map() {
	const { isLoaded } = useJsApiLoader({
		id: "google-map-script",
		googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
	});

	const [map, setMap] = React.useState(null);

	const onLoad = React.useCallback(function callback(map) {
		// This is just an example of getting and using the map instance!!! don't just blindly copy!
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
			{/* Child components, such as markers, info windows, etc. */}
			<></>
		</GoogleMap>
	) : (
		<></>
	);
}

export default Home;
