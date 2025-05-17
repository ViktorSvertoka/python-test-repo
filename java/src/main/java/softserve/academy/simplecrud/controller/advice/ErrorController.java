package softserve.academy.simplecrud.controller.advice;

import jakarta.validation.ConstraintViolationException;
import jakarta.validation.ValidationException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.method.annotation.MethodArgumentConversionNotSupportedException;
import softserve.academy.simplecrud.exception.ProductNotFoundException;

@RestControllerAdvice
public class ErrorController {
    @ExceptionHandler(
            ProductNotFoundException.class
    )
    @ResponseStatus(HttpStatus.NOT_FOUND)
    ErrorDto handleProductNotFoundException(Exception ex) {
        return new ErrorDto(ex.getMessage());
    }

    @ExceptionHandler({
            ValidationException.class,
            MethodArgumentNotValidException.class,
            ConstraintViolationException.class
    })
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    ErrorDto handleValidationException() {
        return new ErrorDto("Invalid data format");
    }

    record ErrorDto(String error) {}
}
