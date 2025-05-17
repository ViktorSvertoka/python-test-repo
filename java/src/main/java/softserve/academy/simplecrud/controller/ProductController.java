package softserve.academy.simplecrud.controller;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import softserve.academy.simplecrud.model.entity.Product;
import softserve.academy.simplecrud.model.request.NewProduct;
import softserve.academy.simplecrud.model.request.PatchProduct;
import softserve.academy.simplecrud.model.response.ProductCreated;
import softserve.academy.simplecrud.model.response.ProductDeleted;
import softserve.academy.simplecrud.model.response.ProductDto;
import softserve.academy.simplecrud.model.response.ProductUpdated;
import softserve.academy.simplecrud.service.ProductService;

import java.util.List;

@RequiredArgsConstructor
@RestController
@RequestMapping("/products")
public class ProductController {
    final ProductService productService;

    @GetMapping
    List<ProductDto> getAll() {
        return productService.getAll();
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    ProductCreated create(
            @Valid @RequestBody NewProduct newProduct
    ) {
        return productService.create(newProduct);
    }

    @GetMapping("/{id}")
    ProductDto getOne(
            @PathVariable String id
    ) {
        return new ProductDto(productService.findById(id));
    }

    @PatchMapping("/{id}")
    ProductUpdated update(
            @Valid @RequestBody PatchProduct patchProduct,
            @PathVariable String id
    ) {
        productService.patch(patchProduct, id);
        return new ProductUpdated();
    }

    @DeleteMapping("/{id}")
    ProductDeleted delete(
            @PathVariable String id
    ) {
        productService.delete(id);
        return new ProductDeleted();
    }
}
