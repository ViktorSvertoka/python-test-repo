package softserve.academy.simplecrud.model.response;

public record ProductUpdated(
        String message
) {
    public ProductUpdated() {
        this("Product updated successfully.");
    }
}
