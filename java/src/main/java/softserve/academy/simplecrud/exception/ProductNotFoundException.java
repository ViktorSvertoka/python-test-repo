package softserve.academy.simplecrud.exception;

public class ProductNotFoundException extends RuntimeException {
    public ProductNotFoundException() {
        super("Not Found");
    }
}
