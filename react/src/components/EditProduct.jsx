import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import {
  patchProduct,
  getProductById as getProductFromApi,
} from "../api/services";

export function EditProduct() {
  const [title, setTitle] = useState("");
  const [price, setPrice] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();
  const { id } = useParams();
  const updateProduct = async (e) => {
    e.preventDefault();
    await patchProduct(id, title, price);
    navigate("/");
  };

  useEffect(() => {
    getProductById();
  }, []);

  const getProductById = async () => {
    const response = await getProductFromApi(id);
    setTitle(response.name);
    setPrice(response.price);
    setIsLoading(false);
  };
  if (isLoading) return <p>Loading...</p>;
  return (
    <div>
      <form onSubmit={updateProduct}>
        <div className="field">
          <label className="label">Title</label>
          <input
            className="input"
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>

        <div className="field">
          <label className="label">Price</label>
          <input
            className="input"
            type="text"
            placeholder="Price"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />
        </div>

        <div className="field">
          <button className="button is-primary">Update</button>
        </div>
      </form>
    </div>
  );
}
