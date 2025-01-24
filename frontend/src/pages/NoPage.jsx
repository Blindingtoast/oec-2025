import React from "react";
import NavDock from "@/components/ui/nav-dock";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";

const NoPage = () => {
	return (
		<>
			<NavDock />
			<Card className="m-10 sm:m-20">
				<CardHeader>
					<CardTitle className="text-2xl">404 there is nothing here!!</CardTitle>
				</CardHeader>

				<CardFooter className="flex justify-between">
					<a href="/">
						<Button>Go Home</Button>
					</a>
				</CardFooter>
			</Card>
		</>
	);
};

export default NoPage;
