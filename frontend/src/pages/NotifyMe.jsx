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
import { PhoneInput } from "@/components/ui/phone-input";

const NotifyMe = () => {
	return (
		<Card className="m-10 sm:m-20 w-max-[900px]">
			<CardHeader>
				<CardTitle>Want to be Notified?</CardTitle>
			</CardHeader>
			<CardContent>
				<form>
					<div className="grid w-full items-center gap-4">
						<div className="flex flex-col space-y-1.5">
							<Label htmlFor="email">Email</Label>
							<Input type="email" id="email" placeholder="Email" required />
						</div>
						<div className="flex flex-col space-y-1.5">
							<Label htmlFor="phoneNumber">Phone Number</Label>
							<PhoneInput required />
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

export default NotifyMe;
