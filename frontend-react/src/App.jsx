import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header/Header.jsx";

function App() {

  return (
      <BrowserRouter>
          <Header />
          <main>
              <div className="container">
                  <div className="app">
                      <Routes>
                          {/*<Route path="/" element={<BrokersPage />} />*/}
                      </Routes>
                  </div>
              </div>
          </main>
      </BrowserRouter>
  )
}

export default App
