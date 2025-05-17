package softserve.academy.simplecrud.model.request;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import jakarta.validation.constraints.Positive;

import java.math.BigDecimal;

public record PatchProduct(
        String name,
        @Positive BigDecimal price
) {
}
