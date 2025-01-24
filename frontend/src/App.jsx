import { useState } from "react";
import "./index.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import ReportForm from "./pages/ReportForm";
import ModifyReport from "./pages/ModifyReport";
import NotifyMe from "./pages/NotifyMe";
import NoPage from "./pages/NoPage";

function App() {
	const [count, setCount] = useState(0);

	return (
		<BrowserRouter>
			<Routes>
				<Route index element={<Home />} />
				<Route path="report/create" element={<ReportForm />} />
				<Route path="report/modify/:id" element={<ModifyReport />} />
				<Route path="notify-me" element={<NotifyMe />} />
				<Route path="*" element={<NoPage />} />
			</Routes>
		</BrowserRouter>
	);
}

export default App;
