import { Footer } from './components/Footer';
import { Header } from './components/Header';
import { ProductList } from './components/ProductList';
import { AddProduct } from './components/AddProduct';
import { NotFound } from './components/NotFound';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { EditProduct } from './components/EditProduct';

function App() {
  return (
    <div className="App">
      <Header />
      <div className="container">
        <div className="columns">
          <div className="column is-half is-offset-one-quarter">
            <BrowserRouter>
              <Routes>
                <Route path="/" element={<ProductList />} />
                <Route path="/add" element={<AddProduct />} />
                <Route path="/edit/:id" element={<EditProduct />} />
                <Route path="*" element={<NotFound />} />
              </Routes>
            </BrowserRouter>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default App;
