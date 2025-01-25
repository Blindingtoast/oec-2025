import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { PhoneInput } from "@/components/ui/phone-input";
import NavDock from "@/components/ui/nav-dock";

const NotifyMe = () => {
    const [email, setEmail] = useState("");
    const [phone, setPhone] = useState("");
    const [location, setLocation] = useState(null);

    const handleSaveClick = () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success, error);
        } else {
            alert("Geolocation not supported");
        }
    };

	const success = (position) => {
		const latitude = position.coords.latitude;
		const longitude = position.coords.longitude;
		setLocation({ latitude, longitude });

		const notifyData = {
			lat: latitude,
			long: longitude,
			email: email,
			phone: phone,
		};

		fetch("/api/users/notifyme", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(notifyData),
		})
			.then((response) => {
				if (response.ok) {
					alert("Notification settings saved successfully");
					window.location.href = "/";
				} else if (response.status === 409) {
					alert("User with this email or phone number already exists");
				} else {
					alert("Error saving notification settings");
				}
			})
			.catch((error) => {
				console.error("Error:", error);
				alert("Error saving notification settings");
			});
	};

    const error = () => {
        alert("Unable to retrieve your location");
    };

    return (
        <>
            <NavDock />
            <Card className="m-10 sm:m-20 w-max-[900px]">
                <CardHeader>
                    <CardTitle>Want to be Notified?</CardTitle>
                </CardHeader>
                <CardContent>
                    <form>
                        <div className="grid w-full items-center gap-4">
                            <div className="flex flex-col space-y-1.5">
                                <Label htmlFor="email">Email</Label>
                                <Input
                                    type="email"
                                    id="email"
                                    placeholder="Email"
                                    required
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                />
                            </div>
                            <div className="flex flex-col space-y-1.5">
                                <Label htmlFor="phoneNumber">Phone Number</Label>
                                <PhoneInput
                                    required
                                    value={phone}
                                    onChange={(value) => setPhone(value)}
                                />
                            </div>
                        </div>
                    </form>
                </CardContent>
                <CardFooter className="flex justify-between">
                    <Button variant="outline">Cancel</Button>
                    <Button onClick={handleSaveClick}>Save</Button>
                </CardFooter>
            </Card>
        </>
    );
};

export default NotifyMe;