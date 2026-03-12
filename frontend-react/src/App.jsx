import {BrowserRouter, Routes, Route} from "react-router-dom";
import Header from "./components/Header/Header.jsx";
import HomePage from "./pages/HomePage/HomePage.jsx";

function App() {
    return (
        <BrowserRouter>
            <Header/>

            <main>
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                </Routes>
            </main>

        </BrowserRouter>
    );
}

export default App;