package softserve.academy.simplecrud.model.request;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Positive;
import org.springframework.validation.annotation.Validated;

import java.math.BigDecimal;

@Validated
public record NewProduct(
        @NotBlank String name,
        @Positive BigDecimal price
) {
}
