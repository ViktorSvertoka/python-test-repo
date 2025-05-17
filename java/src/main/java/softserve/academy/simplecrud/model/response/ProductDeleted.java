package softserve.academy.simplecrud.model.response;

public record ProductDeleted(
        String message
) {
    public ProductDeleted() {
        this("Product deleted.");
    }
}
