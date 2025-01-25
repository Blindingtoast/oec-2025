import React, { useState } from "react";

import { Button } from "@/components/ui/button";
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import NavDock from "@/components/ui/nav-dock";
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select";

const ReportForm = () => {
    const [location, setLocation] = useState(null);
    const [type, setType] = useState("");
    const [description, setDescription] = useState("");

    function handleSaveClick() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success, error);
        } else {
            console.log("Geolocation not supported");
        }
    }

    function success(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        setLocation({ latitude, longitude });
        console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);

        const reportData = {
            lat: latitude,
            long: longitude,
            type: type,
            time: new Date().toISOString().replace('Z', ''),
            description: description,
        };

        fetch("/api/reports/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(reportData),
        })
            .then((response) => {
                if (response.ok) {
                    window.location.href = "/";
                } else {
                    alert("Error submitting report");
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                alert("Error submitting report");
            });
    }

    function error() {
        alert("Unable to retrieve your location");
        console.log("Unable to retrieve your location");
    }

    return (
        <>
            <NavDock />
            <Card className="m-10 sm:m-20 w-max-[900px]">
                <CardHeader>
                    <CardTitle>Add a Disaster</CardTitle>
                    <CardDescription>What is happening around you?</CardDescription>
                </CardHeader>
                <CardContent>
                    <form>
                        <div className="grid w-full items-center gap-4">
                            <div className="flex flex-col space-y-1.5">
                                <Label htmlFor="type" required>
                                    Type of Disaster
                                </Label>
                                <Select onValueChange={(value) => setType(value)}>
                                    <SelectTrigger id="type">
                                        <SelectValue placeholder="Select" />
                                    </SelectTrigger>
                                    <SelectContent position="popper">
                                        <SelectItem value="earthquake">Earthquake</SelectItem>
                                        <SelectItem value="flood">Flood</SelectItem>
                                        <SelectItem value="fire">Fire</SelectItem>
                                        <SelectItem value="hurricane">Hurricane</SelectItem>
                                        <SelectItem value="tornado">Tornado</SelectItem>
                                        <SelectItem value="tsunami">Tsunami</SelectItem>
                                    </SelectContent>
                                </Select>
                            </div>
                            <div className="grid w-full gap-1.5">
                                <Label htmlFor="description">Description</Label>
                                <Textarea
                                    placeholder="Describe what is happening"
                                    id="description"
                                    onChange={(e) => setDescription(e.target.value)}
                                />
                            </div>
                        </div>
                    </form>
                </CardContent>
                <CardFooter className="flex justify-between">
                    <a href="/">
                        <Button variant="outline">Cancel</Button>
                    </a>
                    <Button onClick={handleSaveClick}>Save</Button>
                </CardFooter>
            </Card>
        </>
    );
};

export default ReportForm;