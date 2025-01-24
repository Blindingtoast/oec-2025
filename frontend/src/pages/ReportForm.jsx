import React from "react";

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
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";

const ReportForm = () => {
	return (
		<Card className="m-10 sm:m-20 w-max-[900px]">
			<CardHeader>
				<CardTitle>Add a Disaster</CardTitle>
				<CardDescription>What is happening around you?</CardDescription>
			</CardHeader>
			<CardContent>
				<form>
					<div className="grid w-full items-center gap-4">
						<div className="flex flex-col space-y-1.5">
							<Label htmlFor="name">Name</Label>
							<Input id="name" placeholder="Name of Disaster" />
						</div>
						<div className="flex flex-col space-y-1.5">
							<Label htmlFor="type">Type of Disaster</Label>
							<Select>
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
							<Textarea placeholder="Describe what is happening" id="message" />
						</div>
						<div className="grid w-full gap-1.5">
							<Label htmlFor="resources">Resourses</Label>
							<Textarea placeholder="Add any resources you have" id="message" />
						</div>
					</div>
				</form>
			</CardContent>
			<CardFooter className="flex justify-between">
				<Button variant="outline">Cancel</Button>
				<Button>Save</Button>
			</CardFooter>
		</Card>
	);
};

export default ReportForm;
