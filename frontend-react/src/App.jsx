import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {

  return (
      <BrowserRouter>
          <div className="container">
              <div className="app">
                  <main>
                      <Routes>
                          {/*<Route path="/" element={<BrokersPage />} />*/}
                      </Routes>
                  </main>
              </div>
          </div>
      </BrowserRouter>
  )
}

export default App
