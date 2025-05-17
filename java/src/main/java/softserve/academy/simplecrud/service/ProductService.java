package softserve.academy.simplecrud.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import softserve.academy.simplecrud.exception.ProductNotFoundException;
import softserve.academy.simplecrud.model.entity.Product;
import softserve.academy.simplecrud.model.request.NewProduct;
import softserve.academy.simplecrud.model.request.PatchProduct;
import softserve.academy.simplecrud.model.response.ProductCreated;
import softserve.academy.simplecrud.model.response.ProductDto;
import softserve.academy.simplecrud.repository.ProductRepository;

import java.math.BigDecimal;
import java.util.List;
import java.util.NoSuchElementException;

import static org.springframework.util.StringUtils.hasText;

@RequiredArgsConstructor
@Transactional
@Service
public class ProductService {
    final ProductRepository productRepository;

    @Transactional(readOnly = true)
    public List<ProductDto> getAll() {
        return productRepository.findAll().stream()
                .map(ProductDto::new)
                .toList();
    }

    public ProductCreated create(NewProduct newProduct) {
        Product p = Product.builder()
                .name(newProduct.name())
                .price(newProduct.price())
                .build();
        p = productRepository.save(p);
        return new ProductCreated(p.getId().toString());
    }

    @Transactional(readOnly = true)
    public Product findById(String id) {
        try {
            Long productId = Long.parseLong(id);
            return productRepository.findById(productId).get();
        } catch (NumberFormatException | NoSuchElementException ex) {
            // pass
        }
        throw new ProductNotFoundException();
    }

    public void patch(PatchProduct patchProduct, String id) {
        Product p = findById(id);

        String newName = patchProduct.name();
        if (hasText(newName)) {
            p.setName(newName);
        }

        BigDecimal newPrice = patchProduct.price();
        if (newPrice != null) {
            p.setPrice(newPrice);
        }
        // saved back on transaction closing
    }

    public void delete(String id) {
        Product p = findById(id);
        productRepository.delete(p);
    }
}
