package softserve.academy.simplecrud.model.response;

public record ProductCreated(
        String message,
        String productId
) {
    public ProductCreated(String productId) {
        this("Product added successfully.", productId);
    }
}
